import pytest
from xagents.result_formatter import result_format_agent
from agents import Runner


@pytest.mark.asyncio
async def test_result_formatter():
    example_markdown = """
    search engine: bing
    - **Gold Price Today - Kitco**
      [https://www.kitco.com/gold-price-today](https://www.kitco.com/gold-price-today)  
      Live spot gold prices and charts. Get historical data and news updates on XAUUSD.
    
    - **Shanghai Gold Exchange Daily Price**
      [https://www.sge.com.cn](https://www.sge.com.cn)  
      Official gold trading prices published by the Shanghai Gold Exchange.
    """

    result = await Runner.run(
        input=example_markdown, starting_agent=result_format_agent
    )
    print(result.final_output)
