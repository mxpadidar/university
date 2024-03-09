from typing import Callable, Type

from backbone.service_layer.dtos import Command
from university.domain import commands
from university.service_layer.command_handlers.create_course import (
    create_course_handler,
)

command_handlers: dict[Type[Command], Callable] = {
    commands.CreateCourseCommand: create_course_handler,
}
