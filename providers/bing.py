from providers.base import BaseWebSearchProvider
from config import settings


class BingSearch(BaseWebSearchProvider):
    """
    please check out https://www.bing.com/account/general for more information
    """

    def _get_url(self):
        return f"{settings.bing_search_base_url}"

    def _get_params(self, query: str, **kwargs) -> dict:
        params = {
            "q": query,
            "cc": kwargs.get("cc") or settings.cc,
            "setlang": kwargs.get("lang") or settings.language,
            "form": "QBLH",
        }
        return params


bing_search = BingSearch()
