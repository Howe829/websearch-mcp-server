from providers.bing import bing_search
from providers.base import BaseWebSearchProvider


class WebSearchProviderFactory:
    def get_provider(self, provider_name: str) -> BaseWebSearchProvider:
        match provider_name:
            case "bing":
                return bing_search
            case _:
                raise ValueError
