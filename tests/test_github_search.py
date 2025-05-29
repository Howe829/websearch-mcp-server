import pytest
import re
from providers.factory import WebSearchProviderFactory
from providers.enums import WebSearchProvidersEnum, GithubSearchTypesEnum
from http_client import aio_client


@pytest.mark.parametrize(
    "query, expected",
    [
        ("Qwen3", "Qwen3"),
    ],
)
@pytest.mark.asyncio
async def test_github_search(query, expected):
    factory = WebSearchProviderFactory()
    engine = factory.get_provider(WebSearchProvidersEnum.GITHUB.value)
    result = await engine.search(query, type=GithubSearchTypesEnum.REPO)
    print(result)
    assert expected in result
