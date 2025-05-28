import asyncio
from curl_cffi import AsyncSession
from markitdown import MarkItDown
from io import BytesIO
from config import settings

md = MarkItDown(enable_plugins=False)


class AsyncHttpClient:
    def __init__(self):
        self._session = AsyncSession(impersonate=settings.impersonate)

    async def get(self, url: str, **kwargs) -> str:
        self._session.acurl.loop = asyncio.get_running_loop()
        response = await self._session.get(url=url, **kwargs)
        return response.text

    async def get_markdown(self, url: str, **kwargs) -> str:
        text = await self.get(url=url, **kwargs)
        buffer = BytesIO(text.encode("utf-8"))
        result = md.convert(buffer)
        return result.text_content


aio_client = AsyncHttpClient()
