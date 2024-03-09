from __future__ import annotations

from abc import ABC, abstractmethod

from backbone.adapters.postgres import session_maker
from backbone.domain.abstract_repository import AbstractRepository
from zverifier.adapters.repositories.user_face_repositories import (
    SqlAlchemyUserFaceRepository,
    UserFaceRepository,
)


class AbstractUnitOfWork(ABC):
    repositories: set[AbstractRepository]
    user_face: UserFaceRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    def collect_new_events(self):
        for repo in self.repositories:
            for entity in repo.seen:
                while entity.events:
                    yield entity.events.pop(0)

    @abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class SqlalchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_maker=session_maker) -> None:
        self._session_maker = session_maker
        self.repositories = set()

    def __enter__(self):
        self._session = self._session_maker()
        self.user_face = SqlAlchemyUserFaceRepository(self._session)
        self.repositories.add(self.user_face)
        return super().__enter__()

    def _commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()
