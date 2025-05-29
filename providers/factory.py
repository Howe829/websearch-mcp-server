from providers.base import BaseWebSearchProvider
from providers.enums import WebSearchProvidersEnum
from providers.bing import bing_search
from providers.wechat import wechat_search
from providers.github import github_search
from providers.baidu import baidu_search


class WebSearchProviderFactory:
    def get_provider(self, provider_name: str) -> BaseWebSearchProvider:
        match provider_name:
            case WebSearchProvidersEnum.BAIDU.value:
                return baidu_search
            case WebSearchProvidersEnum.BING.value:
                return bing_search
            case WebSearchProvidersEnum.WECHAT.value:
                return wechat_search
            case WebSearchProvidersEnum.GITHUB.value:
                return github_search
            case _:
                raise ValueError(f"Unsupported provider: [{provider_name}]")
