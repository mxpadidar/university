from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    def __init__(self) -> None:
        self.seen: set = set()

    def add(self, entity):
        self._add(entity)
        self.seen.add(entity)

    @abstractmethod
    def _add(self, entity):
        raise NotImplementedError

    def get_by_id(self, id: int):
        entity = self._get_by_id(id)
        if entity:
            self.seen.add(entity)
        return entity

    @abstractmethod
    def _get_by_id(self, id: int):
        raise NotImplementedError
