import pytest
from http_client import aio_client


@pytest.mark.asyncio
async def test_open_url():
    url = "https://httpbin.org/headers"
    result = await aio_client.get_markdown(url=url, params={})
    print(result)
