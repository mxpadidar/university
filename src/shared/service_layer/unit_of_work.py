from __future__ import annotations

from abc import ABC, abstractmethod

from backbone.adapters.postgres import session_maker
from backbone.domain.abstract_repository import AbstractRepository
from shared.adapters.repositories.file_repositories import (
    FileRepository,
    SqlAlchemyFileRepository,
)


class AbstractUnitOfWork(ABC):
    repositories: set[AbstractRepository]
    file: FileRepository

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
        self.file = SqlAlchemyFileRepository(self._session)
        self.repositories.add(self.file)
        return super().__enter__()

    def _commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()
