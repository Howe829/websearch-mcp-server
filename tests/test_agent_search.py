import pytest
from xagents.agent import agent_search

@pytest.mark.asyncio
async def test_agent_search():
    
    result = await agent_search.search("today's gold price")
    print(result, len(result.items))