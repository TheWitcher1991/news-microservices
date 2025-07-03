from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from services.shared.kernel.error_list import ErrorList
from services.shared.kernel.validation_result import ValidationResult

T = TypeVar("T")


class AbstractValidator(ABC, Generic[T]):

    def __init__(self):
        self.errors = ErrorList([])

    @abstractmethod
    def validate(self, command: T) -> ValidationResult[T]: ...

    def execute(self) -> ValidationResult[T]:
        return ValidationResult(self.errors)