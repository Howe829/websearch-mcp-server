from providers.base import BaseWebSearchProvider


class BaiduSearch(BaseWebSearchProvider):

    def _get_url(self):
        return "https://www.baidu.com/s"

    def _get_params(self, query: str, **kwargs) -> dict:
        params = {
            "wd": query,
        }
        return params


baidu_search = BaiduSearch()