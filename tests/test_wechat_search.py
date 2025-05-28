import pytest
import re
from providers.factory import WebSearchProviderFactory
from providers.enums import WebSearchProvidersEnum
from http_client import aio_client


@pytest.mark.parametrize(
    "query, expected",
    [
        ("Qwen3", "Qwen3"),
    ],
)
@pytest.mark.asyncio
async def test_wechat_search(query, expected):
    factory = WebSearchProviderFactory()
    engine = factory.get_provider(WebSearchProvidersEnum.WECHAT.value)
    result = await engine.search(query)
    assert expected in result


@pytest.mark.asyncio
async def test_open_wechat_article_link():
    base_url = "https://weixin.sogou.com"

    link = "/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS8ijmarRqdrqbhEu2sEWJ9vwrgtPQfuWoVqXa8Fplpd9iOBwqPAAVnXSO9z52qOk4rwgK6xj4NQCkHfsLwEwgPn59x5W2xuVD-gx0MAr_9dfL808_OJlX3gYfmcE5YmIf2SfHBPkjCsQRTAfP6vRdpXW7foMB4Dvm0oBCYb7hoL6BVTE-TilKeJfP1s2uOjBc5Jh3jb43a-vUjKzlnuO_HBFkDr8IT4KYw..&type=2&query=ANP&token=8849B446BF96DC62101626381EF02B4111D511AF683676E8"
    url = f"{base_url}{link}"

    result = await aio_client.get(url)
    parts = re.findall(r"url\s*\+=\s*'([^']+)'", result)
    full_url = "".join(parts)
    print(full_url)
    text = await aio_client.get_markdown(full_url)
    print(text)
    assert "var url" in result
