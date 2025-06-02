from providers.base import BaseWebSearchProvider
from config import settings
from http_client import aio_client


class GoogleSearch(BaseWebSearchProvider):
    def _get_url(self):
        return f"{settings.google_search_base_url}/search"

    def _get_params(self, query: str, **kwargs) -> dict:
        cc = kwargs.get("cc") or settings.cc
        lang = kwargs.get("lang") or settings.language
        params = {
            "q": query,
            "lr": f"lang_{lang}",
            "cr": f"country{cc.upper()}",
        }
        return params

    async def search(self, query: str, use_browser: bool = True, **kwargs) -> str:
        url = self._get_url()
        params = self._get_params(query=query, **kwargs)
        return await aio_client.get_markdown(
            url=url,
            params=params,
            use_browser=True,  # google search must use browser to query
        )


google_search = GoogleSearch()
