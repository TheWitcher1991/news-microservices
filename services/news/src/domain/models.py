from datetime import datetime

from services.news.src.domain.enums import PostStatus
from services.news.src.domain.value_objects import PostId


class Post:
    id: PostId
    title: str
    description: str
    status: PostStatus
    created_at: datetime
    updated_at: datetime

    def __init__(
        self,
        id: PostId,
        title: str,
        description: str,
        status: PostStatus = PostStatus.DRAFT,
        created_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now()
    ):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, Post):
            return self.id == obj.id

        return False

    @staticmethod
    def create(title: str, description: str) -> "Post":
        return Post(
            PostId.generate(),
            title,
            description
        )
