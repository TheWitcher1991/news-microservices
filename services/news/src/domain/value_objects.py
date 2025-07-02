from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True)
class PostId:

    value: UUID

    @staticmethod
    def generate() -> "PostId":
        return PostId(uuid4())

    def __str__(self) -> str:
        return str(self.value)
