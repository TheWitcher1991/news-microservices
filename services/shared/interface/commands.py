from abc import ABC, abstractmethod

from services.shared.kernel.result import Result


class Command(ABC):
    pass


class CommandHandler(ABC):
    @abstractmethod
    def handle(self, command: Command) -> Result:
        pass
