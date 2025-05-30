import pytest
from providers.factory import WebSearchProviderFactory
from providers.enums import WebSearchProvidersEnum


@pytest.mark.parametrize(
    "query, cc, lang, expected",
    [
        ("What is the weather like in Shanghai?", "cn", "zh-CN", "没有与此相关的结果"),
        ("What is the weather like in Shanghai?", "us", "en", ""),
    ],
)
@pytest.mark.asyncio
async def test_bing_search(query, cc, lang, expected):
    factory = WebSearchProviderFactory()
    engine = factory.get_provider(WebSearchProvidersEnum.BING.value)
    result = await engine.search(query, cc=cc, lang=lang)
    assert expected in result
