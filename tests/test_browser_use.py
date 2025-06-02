import pytest
from http_client import aio_client


@pytest.mark.asyncio
async def test_browser_use():
    url = "https://www.google.com/search"
    params = {"q": "iphone16pro"}
    result = await aio_client.get_markdown(url, params, use_browser=True)
    print(result)
