from providers.base import BaseWebSearchProvider
from config import settings
from typing import Optional


class WechatSearch(BaseWebSearchProvider):
    """
    https://weixin.sogou.com
    """

    def _get_url(self):
        return "https://weixin.sogou.com/weixin"

    def _get_params(
        self, query: str, cc: Optional[str] = None, lang: Optional[str] = None
    ) -> dict:
        params = {"query": query, "type": 2}
        return params


wechat_search = WechatSearch()
