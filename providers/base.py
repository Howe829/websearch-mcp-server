from abc import abstractmethod
from pydantic import BaseModel
from config import settings
from http_client import aio_client
from typing import Optional


class BaseWebSearchProvider(BaseModel):
    @abstractmethod
    def _get_url(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def _get_params(
        self, query: str, cc: Optional[str] = None, lang: Optional[str] = None
    ) -> dict:
        raise NotImplementedError

    async def search(
        self, query: str, cc: Optional[str] = None, lang: Optional[str] = None, **kwargs
    ) -> str:
        url = self._get_url()
        params = self._get_params(query=query, cc=cc, lang=lang)
        return await aio_client.get_markdown(
            url=url, params=params, impersonate=settings.impersonate, **kwargs
        )
