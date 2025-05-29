from abc import abstractmethod
from pydantic import BaseModel
from config import settings
from http_client import aio_client


class BaseWebSearchProvider(BaseModel):
    @abstractmethod
    def _get_url(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def _get_params(self, query: str, **kwargs) -> dict:
        raise NotImplementedError

    async def search(self, query: str, **kwargs) -> str:
        url = self._get_url()
        params = self._get_params(query=query, **kwargs)
        return await aio_client.get_markdown(
            url=url, params=params, impersonate=settings.impersonate
        )
