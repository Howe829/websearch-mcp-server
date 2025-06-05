from providers.base import BaseWebSearchProvider


class BaiduSearch(BaseWebSearchProvider):
    def _get_url(self):
        return "https://www.baidu.com/s"

    def _get_params(self, query: str, **kwargs) -> dict:
        params = {
            "wd": query,
        }
        return params

    @property
    def description(self):
        return """
        Strengths:
        - Strong understanding of Chinese language and entity recognition
        - Better coverage of local Chinese content (government, regional news, company sites)
        - Excellent performance with brand names and trending topics
        - Fast, responsive search experience
        
        Weaknesses:
        - Weak support for English-language queries
        - Limited support for structured queries (e.g., Boolean logic, site:, filetype:)
        - Poor international or technical content retrieval compared to Bing or Google
        
        Query Strategy:
        - For Chinese: Use natural language phrasing with brand or location keywords (e.g., “今日金价 上海黄金交易所”)
        - Avoid complex English queries; translate and rephrase into Chinese where possible
        - Emphasize relevance over syntax — focus on intent expression
        """


baidu_search = BaiduSearch()
