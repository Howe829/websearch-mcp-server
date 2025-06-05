import re
import asyncio
from fastmcp import FastMCP
from urllib.parse import urljoin
from typing import Literal

from providers.factory import WebSearchProviderFactory
from providers.enums import WebSearchProvidersEnum, GithubSearchTypesEnum
from http_client import aio_client
from config import settings
from xagents.agent import agent_search, SearchResult

server = FastMCP("WebSearch MCP Server")

provider_factory = WebSearchProviderFactory()

@server.tool(name="AgentSearch")
async def agent_search_tool(
    query: str,
) -> SearchResult:
    """
    Perform a agentic search

    Args:
        query: The search query.

    Returns:
        instance of SearchResult
    """
    return await agent_search.search(query)
    

@server.tool(name="BingSearch")
async def bing_search(
    query: str,
    cc: str = "us",
    lang: str = "en",
    use_browser: bool = False,
) -> str:
    """
    Perform a bing search.

    Args:
        query: The search query.
        cc: Country/Region code for example: us, cn, jp, etc.
        lang: Language such as en, zh-CN, ja, etc
        use_browser: Whether to use a browser to query, you must try use_browser=False first

    Returns:
        Search result in markdown syntax.
    """

    engine = provider_factory.get_provider(
        provider_name=WebSearchProvidersEnum.BING.value
    )
    result = await engine.search(query=query, use_browser=use_browser, cc=cc, lang=lang)
    return result


@server.tool(name="BaiduSearch")
async def baidu_search(
    query: str,
    use_browser: bool = False,
) -> str:
    """
    Perform a baidu search.

    Args:
        query: The search query.
        use_browser: Whether to use a browser to query, you must try use_browser=False first

    Returns:
        Search result in markdown syntax.
    """

    engine = provider_factory.get_provider(
        provider_name=WebSearchProvidersEnum.BAIDU.value
    )
    result = await engine.search(query=query, use_browser=use_browser)
    return result


@server.tool(name="GoogleSearch")
async def websearch(
    query: str,
    cc: str = "us",
    lang: str = "en",
) -> str:
    """
    Perform a google search.

     Args:
         query: The search query.
         cc: Country/Region code for example: us, cn, jp, etc.
         lang: Language such as en, zh-CN, ja, etc

     Returns:
         Search result in markdown syntax.
    """

    engine = provider_factory.get_provider(
        provider_name=WebSearchProvidersEnum.GOOGLE.value
    )
    result = await engine.search(query=query, cc=cc, lang=lang)
    return result


@server.tool(name="OpenUrl")
async def open_url(url: str) -> str:
    """
    Open a URL and retrieve its content.

    Args:
        url: The URL to be opened.

    Returns:
        Web content in markdown syntax.
    """
    return await aio_client.get_markdown(url)


@server.tool(name="OpenWechatArticleLink")
async def open_wechat_article_link(link: str) -> dict:
    """
    Open a wechat article link and retrieve its content.
    Remember you have to do the WechatSearch first before you open the link, otherwise it will be failed

    Args:
        url: The URL to be opened.Generally starts with '/link'

    Returns:
        Web content in markdown syntax.
    """
    url = urljoin("https://weixin.sogou.com", link)
    result = await aio_client.get(url)
    parts = re.findall(r"url\s*\+=\s*'([^']+)'", result)
    full_url = "".join(parts)
    if not full_url.startswith("https"):
        return {"error": f"bad request with link [{link}]"}
    text = await aio_client.get_markdown(full_url)
    return {"url": full_url, "content": text}


@server.tool(name="WechatSearch")
async def wechat_search(query: str) -> str:
    """
    Search WeChat Articles
    Args:
        query: search query.

    Returns:
        Search result in markdown syntax.
    """

    engine = provider_factory.get_provider(
        provider_name=WebSearchProvidersEnum.WECHAT.value
    )
    result = await engine.search(query=query)
    return result


@server.tool(name="GithubSearch")
async def github_search(
    query: str,
    type: Literal[
        GithubSearchTypesEnum.REPO,
        GithubSearchTypesEnum.CODE,
        GithubSearchTypesEnum.ISSUE,
        GithubSearchTypesEnum.PR,
        GithubSearchTypesEnum.DISCUSS,
        GithubSearchTypesEnum.USER,
        GithubSearchTypesEnum.COMMIT,
        GithubSearchTypesEnum.PACKAGE,
        GithubSearchTypesEnum.WIKI,
        GithubSearchTypesEnum.TOPIC,
        GithubSearchTypesEnum.MARKETPLACE,
    ],
    page: int = 1,
) -> str:
    """
    Search All Github
    Args:
        query: search query.
        type: search type support: repositoris, code, issues, pullrequests, users, discussions, commits, packages, wikis, topics, marketplace.
        page: pagination param default is 1

    Returns:
        Search result in markdown syntax.
    """

    engine = provider_factory.get_provider(
        provider_name=WebSearchProvidersEnum.GITHUB.value
    )
    result = await engine.search(query=query, type=type, page=page)
    return result


async def main():
    match settings.server_mode:
        case "stdio":
            await server.run_async(transport=settings.server_mode)
        case "sse" | "streamable-http":
            await server.run_async(
                transport=settings.server_mode, host=settings.host, port=settings.port
            )
        case _:
            raise ValueError(f"Unsupported server mode [{settings.server_mode}]")


if __name__ == "__main__":
    asyncio.run(main())
