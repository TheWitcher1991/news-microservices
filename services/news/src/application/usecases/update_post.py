from abc import abstractmethod

from services.news.src.domain.enums import PostStatus
from services.news.src.domain.exceptions import PostNotFoundError
from services.news.src.domain.models import Post
from services.news.src.domain.uow import PostUnitOfWork
from services.news.src.domain.value_objects import PostId
from services.shared.interface.usecases import AbstractUseCase


class UpdatePostUseCase(AbstractUseCase):

    @abstractmethod
    def execute(self, id: PostId, title: str, description: str, status: PostStatus) -> Post: ...


class UpdatePostUseCaseImpl(UpdatePostUseCase):
    def __init__(self, uow: PostUnitOfWork):
        self.uow = uow

    def execute(self, id: PostId, title: str, description: str, status: PostStatus) -> Post:
        post = self.uow.repository.find_by_id(int(id))

        if post is None:
            raise PostNotFoundError

        post.title = title
        post.description = description
        post.status = status

        try:
            self.uow.repository.update(post)
            self.uow.commit()
        except Exception as e:
            self.uow.rollback()

        return post
