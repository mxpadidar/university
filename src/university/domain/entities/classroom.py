from backbone.domain.abstract_entity import AbstractEntity


class Classroom(AbstractEntity):
    id: int
    location: str
    lat: float
    lng: float
    capacity: int
    title: str
