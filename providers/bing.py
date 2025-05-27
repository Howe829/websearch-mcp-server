from providers.base import BaseWebSearchProvider
from config import settings


class BingSearch(BaseWebSearchProvider):
    """
    please check out https://www.bing.com/account/general for more information
    """

    def _get_url(self):
        return f"{settings.bing_search_base_url}/search"

    def _get_params(self, query: str, cc:str = None, lang: str = None) -> dict:
        params = {"q": query, "cc": cc or  settings.cc, "setlang": lang or settings.language}
        return params


bing_search = BingSearch()
