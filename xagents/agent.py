from agents import Runner
from pydantic import BaseModel
from asyncio import TaskGroup
from loguru import logger

from xagents.query_optimizer import query_opt_agent, WebSearchPlan, WebSearchItem
from xagents.result_formatter import result_format_agent, SearchResult
from providers.factory import WebSearchProviderFactory


class RawSearchResult(BaseModel):
    engine_name: str
    content: str


class AgentSearch:
    async def _optimize_query(self, query: str) -> WebSearchPlan:
        result = await Runner.run(input=query, starting_agent=query_opt_agent)
        return result.final_output_as(WebSearchPlan)

    async def _perform_search(self, item: WebSearchItem) -> RawSearchResult:
        engine = WebSearchProviderFactory().get_provider(item.engine_name)
        result = await engine.search(query=item.query, use_browser=True)
        return RawSearchResult(engine_name=item.engine_name, content=result)

    async def _format_result(self, raw_result: RawSearchResult) -> SearchResult:
        result = await Runner.run(
            input=raw_result.model_dump_json(), starting_agent=result_format_agent
        )
        return result.final_output_as(SearchResult)

    async def _execute_search_plan(self, plan: WebSearchPlan) -> list[RawSearchResult]:
        tasks = []
        async with TaskGroup() as tg:
            for search_item in plan.searches:
                task = tg.create_task(self._perform_search(search_item))
                tasks.append(task)

        results: list[RawSearchResult] = [t.result() for t in tasks]
        return results

    def _merge_search_results(self, search_results: list[SearchResult]) -> SearchResult:
        items = []
        for r in search_results:
            items.extend(r.items)
        return SearchResult(items=items)

    async def search(self, query: str) -> SearchResult:
        search_plan = await self._optimize_query(query=query)
        raw_results = await self._execute_search_plan(plan=search_plan)
        tasks = []
        async with TaskGroup() as tg:
            for raw_result in raw_results:
                task = tg.create_task(self._format_result(raw_result))
                tasks.append(task)
        results: list[SearchResult] = [t.result() for t in tasks]
        return self._merge_search_results(results)

agent_search = AgentSearch()