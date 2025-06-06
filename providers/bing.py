from providers.base import BaseWebSearchProvider
from config import settings


class BingSearch(BaseWebSearchProvider):
    """
    please check out https://www.bing.com/account/general for more information
    """

    def _get_url(self):
        return f"{settings.bing_search_base_url}/search"

    def _get_params(self, query: str, **kwargs) -> dict:
        params = {
            "q": query,
            "cc": kwargs.get("cc") or settings.cc,
            "setlang": kwargs.get("lang") or settings.language,
        }
        return params

    @property
    def description(self):
        return """
        Strengths:
        - Excellent support for English queries
        - Handles structured search operators well (site:, filetype:, before:, after:, etc.)
        - Good at answering natural language questions (especially in English)
        - Strong performance for technical, coding, and international finance topics
        
        Weaknesses:
        - Less effective at retrieving localized Chinese content
        - Sometimes inferior Chinese-language result quality compared to Baidu
        
        Query Strategy:
        - For English: Use precise keywords + operators (e.g., `gold price today site:kitco.com`)
        - For Chinese: Keep queries concise but add intent-enhancing modifiers (e.g., “实时”, “走势图”)
        - Prefer Bing for technical, financial, or global information needs
        """


bing_search = BingSearch()
