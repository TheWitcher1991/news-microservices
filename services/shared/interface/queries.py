from abc import ABC, abstractmethod

from sqlalchemy import Result


class Query(ABC):
    pass


class QueryHandler(ABC):
    @abstractmethod
    def handle(self, query: Query) -> Result:
        pass
