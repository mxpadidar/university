from typing import Callable, Type

from backbone.service_layer.dtos import Event
from university.domain import events
from university.service_layer.event_handlers.course_created import (
    course_created_handler,
)

event_handlers: dict[Type[Event], list[Callable]] = {
    events.CourseCreatedEvent: [course_created_handler],
}
