from backbone.domain.abstract_entity import AbstractEntity
from backbone.domain.enums import EntityType


class University(AbstractEntity):
    id: int
    name: str
    city: str

    @classmethod
    def create(cls, name: str, city: str) -> "University":
        university = cls()
        university.name = name
        university.city = city
        return university

    @classmethod
    def entity_type(cls) -> EntityType:
        return EntityType.UNIVERSITY
