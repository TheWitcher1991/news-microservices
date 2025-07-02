from enum import Enum


class PostStatus(Enum):
    DRAFT = "draft"
    PUBLISHED = "published"

    def __str__(self) -> str:
        return self.value
