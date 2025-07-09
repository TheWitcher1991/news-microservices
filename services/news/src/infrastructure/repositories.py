from typing import List, Sequence

from services.news.src.domain.models import Post
from services.news.src.domain.repositories import PostRepository
from services.news.src.domain.value_objects import PostId
from services.news.src.infrastructure.models import PostDTO
from services.news.src.presentation.request import PostFilter
from sqlalchemy import and_, desc, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session


class PostRepositoryImpl(PostRepository):

    def __init__(self, session: Session):
        self.session = session

    def create(self, entity: Post) -> Post:
        task = PostDTO.from_entity(entity)

        self.session.add(task)

        return task.to_entity()

    def save(self, entity: Post) -> None:
        dto = PostDTO.from_entity(entity)

        try:
            existing = self.session.get(PostDTO, entity.id.value)
        except NoResultFound:
            self.session.add(dto)
        else:
            existing.title = dto.title
            existing.description = dto.description
            existing.status = dto.status
            existing.created_at = dto.created_at
            existing.updated_at = dto.updated_at

    def update(self, entity: Post) -> None:
        dto = PostDTO.from_entity(entity)

        self.session.query(PostDTO).filter_by(id=dto.id).update(
            {
                "title": dto.title,
                "description": dto.description,
                "status": dto.status,
                "created_at": dto.created_at,
                "updated_at": dto.updated_at,
            }
        )

    def find_all(self, filters: PostFilter) -> List[Post]:
        stmt = select(PostDTO).order_by(desc(PostDTO.created_at))

        conditions = []

        if filters.title:
            conditions.append(PostDTO.title.ilike(f"%{filters.title}%"))
        if filters.status:
            conditions.append(PostDTO.status == filters.status.value)

        if conditions:
            stmt = stmt.where(and_(*conditions))

        try:
            result: Sequence[PostDTO] = self.session.execute(stmt).scalars().all()
        except NoResultFound:
            return []

        return [dto.to_entity() for dto in result]

    def find_by_id(self, id_: PostId) -> Post | None:
        result: PostDTO | None = self.session.get(PostDTO, id_.value)

        if result is None:
            return None

        return result.to_entity()

    def delete(self, id_: PostId):
        self.session.query(PostDTO).filter_by(id=id_.value).delete()
