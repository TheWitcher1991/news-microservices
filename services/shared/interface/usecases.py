from abc import ABC, abstractmethod
from typing import Generic, TypeVar

_T = TypeVar('_T')
_R = TypeVar('_R')


class AbstractUseCase(ABC, Generic[_T, _R]):

    @abstractmethod
    def execute(self, **args: _T) -> _R:
        raise NotImplementedError()
