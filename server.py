import asyncio
from fastmcp import FastMCP

from providers.factory import WebSearchProviderFactory
from http_client import aio_client
from config import settings

server = FastMCP("WebSearch MCP Server")


@server.tool()
async def websearch(query: str, provider_name: str = "bing") -> str:
    """
    Perform a web search.

    Args:
        query: The search query.
        provider_name: The search engine provider (currently only supports 'bing').

    Returns:
        Search result in markdown syntax.
    """

    factory = WebSearchProviderFactory()
    engine = factory.get_provider(provider_name=provider_name)
    result = await engine.search(query=query)
    return result


@server.tool()
async def open_url(url: str) -> str:
    """
    Open a URL and retrieve its content.

    Args:
        url: The URL to be opened.

    Returns:
        Web content in markdown syntax.
    """
    return await aio_client.get_markdown(url)

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
