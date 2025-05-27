import pytest
from providers.factory import WebSearchProviderFactory

@pytest.mark.parametrize("cc, lang, expected", [
    ("cn", "zh-Hans", "没有与此相关的结果"),
    ("us", "en", ""),
])
@pytest.mark.asyncio
async def test_bing_search(cc, lang, expected):

    factory = WebSearchProviderFactory()
    engine = factory.get_provider("bing")
    result = await engine.search("What is the weather like in Shanghai?", cc=cc, lang=lang)
    assert expected in result