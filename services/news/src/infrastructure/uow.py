from services.news.src.domain.repositories import PostRepository
from services.news.src.domain.uow import PostUnitOfWork
from sqlalchemy.orm import Session


class PostUnitOfWorkImpl(PostUnitOfWork):

    def __init__(self, session: Session, repository: PostRepository):
        self.session: Session = session
        self.repository: PostRepository = repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
