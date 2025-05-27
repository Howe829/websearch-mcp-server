from curl_cffi import AsyncSession
from markitdown import MarkItDown
from io import BytesIO

md = MarkItDown(enable_plugins=False)


class AsyncHttpClient:

    async def get(self, url: str, **kwargs) -> str:
        async with AsyncSession() as client:
            response = await client.get(url=url, **kwargs)
            return response.text

    async def get_markdown(self, url: str, **kwargs) -> str:
        text = await self.get(url=url, **kwargs)
        buffer = BytesIO(text.encode("utf-8"))
        result = md.convert(buffer)
        return result.text_content


aio_client = AsyncHttpClient()
