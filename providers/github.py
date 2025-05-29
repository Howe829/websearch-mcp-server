from providers.base import BaseWebSearchProvider
from providers.enums import GithubSearchTypesEnum


class GithubSearch(BaseWebSearchProvider):
    """
    https://www.github.com
    """

    def _get_url(self):
        return "https://www.github.com/search"

    def _get_params(self, query: str, **kwargs) -> dict:
        params = {
            "q": query,
            "type": kwargs.get("type", GithubSearchTypesEnum.REPO.value),
        }
        return params


github_search = GithubSearch()
