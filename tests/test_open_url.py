import pytest
from http_client import aio_client

@pytest.mark.asyncio
async def test_open_url():
    url = "https://www.qq.com"
    result = await aio_client.get_markdown(url=url, impersonate="edge")
    print(result)