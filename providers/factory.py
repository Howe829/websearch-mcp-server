from providers.bing import bing_search
from providers.base import BaseWebSearchProvider
from providers.wechat import wechat_search
from providers.enums import WebSearchProvidersEnum


class WebSearchProviderFactory:
    def get_provider(self, provider_name: str) -> BaseWebSearchProvider:
        match provider_name:
            case WebSearchProvidersEnum.BING.value:
                return bing_search
            case WebSearchProvidersEnum.WECHAT.value:
                return wechat_search
            case _:
                raise ValueError
