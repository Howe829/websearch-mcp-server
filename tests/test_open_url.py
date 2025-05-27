import pytest
from http_client import aio_client

@pytest.mark.asyncio
async def test_open_url():
    url = "https://www.bing.com"
    result = await aio_client.get(url=url)
    print(result)