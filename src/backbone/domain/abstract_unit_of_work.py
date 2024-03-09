from __future__ import annotations

from abc import ABC, abstractmethod

from backbone.domain.abstract_repository import AbstractRepository


class AbstractUnitOfWork(ABC):
    repositories: set[AbstractRepository]

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
