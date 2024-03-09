from dataclasses import dataclass

from backbone.service_layer.dtos import Event


@dataclass(frozen=True)
class CourseCreatedEvent(Event):
    event_title: str
