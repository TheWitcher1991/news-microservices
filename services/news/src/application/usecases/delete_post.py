from abc import abstractmethod

from services.news.src.domain.exceptions import PostNotFoundError
from services.news.src.domain.repositories import PostRepository
from services.news.src.domain.value_objects import PostId
from services.shared.interface.usecases import AbstractUseCase


class DeletePostUseCase(AbstractUseCase):

    @abstractmethod
    def execute(self, id: PostId) -> None: ...


class DeletePostUseCaseImpl(DeletePostUseCase):
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def execute(self, id: PostId) -> None:
        post = self.post_repository.find_by_id(int(id))

        if post is None:
            raise PostNotFoundError

        self.post_repository.delete(int(id))
