from uuid import UUID

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from services.news.src.domain.enums import PostStatus
from services.news.src.domain.models import Post
from services.news.src.domain.value_objects import PostId
from services.news.src.infrastructure.database import Base


class PostDTO(Base):
    __tablename__ = 'posts'

    id: Mapped[UUID] = mapped_column(primary_key=True, autoincrement=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(3000), nullable=False)
    status: Mapped[str] = mapped_column(index=True, nullable=False)
    created_at: Mapped[int] = mapped_column(index=True, nullable=False)
    updated_at: Mapped[int] = mapped_column(index=True, nullable=False)

    def to_entity(self) -> Post:
        return Post(
            id=PostId(self.id),
            title=self.title,
            description=self.description,
            status=PostStatus(self.status),
            created_at=self.created_at,
            updated_at=self.updated_at
        )

    @staticmethod
    def from_entity(post: Post) -> 'PostDTO':
        return PostDTO(
            id=post.id.value,
            title=post.title,
            description=post.description,
            status=post.status.value,
            created_at=post.created_at,
            updated_at=post.updated_at
        )