from pydantic import BaseModel, Field
from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel
from config import settings

class SearchResultItem(BaseModel):
    title: str = Field(description="search item title")
    description: str = Field(description="search item description")
    source_url: str = Field(description="search item source url")
    engine:str = Field(description="search engine name")

class SearchResult(BaseModel):
    items: list[SearchResultItem]

INSTRCUTION = """
You are a Search Result Formatter Agent.

Your task is to extract structured search result items from unstructured or semi-structured search result content written in Markdown.

Each result must be extracted as a SearchResultItem object with the following fields:
- title: The clickable title of the result (typically found in bold or header formatting).
- description: A concise summary or snippet describing the content of the result.
- source_url: The original source URL (typically found in parentheses or Markdown links).

---

🧪 Input Format:
You will receive search results formatted in Markdown, for example:

- **Gold Price Today - Kitco**
  [https://www.kitco.com/gold-price-today](https://www.kitco.com/gold-price-today)  
  Live spot gold prices and charts. Get historical data and news updates on XAUUSD.

- **Shanghai Gold Exchange Daily Price**
  [https://www.sge.com.cn](https://www.sge.com.cn)  
  Official gold trading prices published by the Shanghai Gold Exchange.

---

✅ Extraction Rules:
1. For each search engine group (e.g., Bing, Baidu), extract **at most the top 3 results**.
2. Extract each result as one `SearchResultItem`.
3. If a result has multiple lines, group them based on proximity (title + description + link).
4. Ignore Markdown formatting — only extract plain text content.
5. If any field is missing, skip the entry.
6. Return a **JSON array** of SearchResultItem objects.
"""
result_format_agent = Agent(
    name="ResultFormatAgent",
    instructions=INSTRCUTION,
    model=LitellmModel(model=f"openai/{settings.llm_model_name}", base_url=settings.llm_base_url, api_key=settings.llm_api_key),
    output_type=SearchResult
)