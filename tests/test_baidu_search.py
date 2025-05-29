import pytest
from providers.factory import WebSearchProviderFactory
from providers.enums import WebSearchProvidersEnum


@pytest.mark.parametrize(
    "query, expected",
    [
        ("deepseek-r1", "deepseek-r1")
    ],
)
@pytest.mark.asyncio
async def test_baidu_search(query, expected):
    factory = WebSearchProviderFactory()
    engine = factory.get_provider(WebSearchProvidersEnum.BAIDU.value)
    result = await engine.search(
        query
    )
    assert expected in result
