import pytest
from xagents.query_optimizer import query_opt_agent
from agents import Runner


@pytest.mark.asyncio
async def test_query_optimizer():
    result = await Runner.run(
        input="查询语句：今日金价", starting_agent=query_opt_agent
    )
    print(result.final_output)
