import asyncio
from os import name
from curl_cffi.requests import impersonate
from fastmcp import FastMCP

from providers.factory import WebSearchProviderFactory
from http_client import aio_client
from config import settings

server = FastMCP("WebSearch MCP Server")


@server.tool(name="WebSearch")
async def websearch(query: str, provider_name: str = "bing", cc: str = "us", lang: str = "en") -> str:
    """
    Perform a web search.

    Args:
        query: The search query.
        provider_name: The search engine provider (currently only supports 'bing').
        cc: Country/Region code for example: us, cn, jp, etc.
        lang: Language such as en, zh-Hans, ja, etc

    Returns:
        Search result in markdown syntax.
    """

    factory = WebSearchProviderFactory()
    engine = factory.get_provider(provider_name=provider_name)
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
    return await aio_client.get_markdown(url, impersonate=settings.impersonate)

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
