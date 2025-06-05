import asyncio
import sys
import nodriver as uc
from curl_cffi import requests, AsyncSession
from markitdown import MarkItDown
from io import BytesIO
from requests import Request
from typing import Optional
from config import settings

md = MarkItDown(enable_plugins=False)


class AsyncHttpClient:
    def __init__(self):
        if self.is_windows:
            self._session = requests.Session(impersonate=settings.impersonate)
        else:
            self._session = AsyncSession(impersonate=settings.impersonate)

    @property
    def is_windows(self):
        return sys.platform.startswith("win")

    async def _get_by_curl_async(self, url: str, params: Optional[dict]) -> str:
        self._session.acurl.loop = asyncio.get_running_loop()
        response = await self._session.get(url=url, params=params)
        return response.text

    def _get_by_curl(self, url: str, params: Optional[dict]) -> str:
        response = self._session.get(url=url, params=params)
        return response.text

    async def _get_by_browser(self, url: str, params: Optional[dict]) -> str:
        driver = await uc.start()
        try:
            req = Request("GET", url, params=params).prepare()
            url = req.url if req.url is not None else url
            tab = await driver.get(url)
            await asyncio.sleep(5)
            text = await tab.get_content()
            return text
        except Exception as e:
            return f"Error when using browser: {str(e)}"
        finally:
            driver.stop()

    async def get(
        self, url: str, params: Optional[dict] = None, use_browser: bool = False
    ) -> str:
        if use_browser:
            return await self._get_by_browser(url, params)
        if self.is_windows:
            return self._get_by_curl(url, params)
        return await self._get_by_curl_async(url, params)

    async def get_markdown(
        self, url: str, params: Optional[dict] = None, use_browser: bool = False
    ) -> str:
        text = await self.get(url=url, params=params, use_browser=use_browser)
        buffer = BytesIO(text.encode("utf-8"))
        result = md.convert(buffer)
        return result.text_content


aio_client = AsyncHttpClient()
