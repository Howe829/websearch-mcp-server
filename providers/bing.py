from providers.base import BaseWebSearchProvider
from config import settings
from typing import Optional


class BingSearch(BaseWebSearchProvider):
    """
    please check out https://www.bing.com/account/general for more information
    """

    def _get_url(self):
        return f"{settings.bing_search_base_url}"

    def _get_params(
        self, query: str, cc: Optional[str] = None, lang: Optional[str] = None
    ) -> dict:
        params = {
            "q": query,
            "cc": cc or settings.cc,
            "setlang": lang or settings.language,
            "form": "QBLH"
        }
        return params


bing_search = BingSearch()
