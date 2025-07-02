from abc import ABC, abstractmethod
from typing import TypeVar, List, Generic

_T = TypeVar('_T')


class AbstractRepository(ABC, Generic[_T]):

    @abstractmethod
    def save(self, entity: _T) -> _T:
        raise NotImplementedError()

    @abstractmethod
    def create(self, entity: _T) -> _T:
        raise NotImplementedError()

    @abstractmethod
    def find_all(self) -> List[_T]:
        raise NotImplementedError()

    @abstractmethod
    def find_by_id(self, id_: int) -> _T | None:
        raise NotImplementedError()

    @abstractmethod
    def update(self, entity: _T) -> _T:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, id_: int) -> None:
        raise NotImplementedError()
