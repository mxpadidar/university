from abc import ABC, abstractmethod

from backbone.domain.enums import EntityType


class AbstractEntity(ABC):

    def to_dict(self) -> dict:
        return self.__dict__

    @classmethod
    @abstractmethod
    def entity_type(cls) -> EntityType: ...
