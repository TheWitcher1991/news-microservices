from fastapi import APIRouter


class NewsRouter:
    def __init__(self):
        self.router = APIRouter(tags=["News"])
        self.include_routers()

    def include_routers(self):
        pass
