from typing import Callable, Type

from backbone.domain.abstract_unit_of_work import AbstractUnitOfWork
from backbone.service_layer.dtos import Command, Event


class MessageBus:
    def __init__(
        self,
        uow: AbstractUnitOfWork,
        event_handlers: dict[Type[Event], list[Callable]],
        command_handlers: dict[Type[Command], Callable],
    ):
        self._uow = uow
        self._event_handlers = event_handlers
        self._command_handlers = command_handlers

    def handle(self, message: Event | Command):
        self.queue = [message]
        while self.queue:
            message = self.queue.pop(0)

            if isinstance(message, Event):
                self.handle_event(message)

            elif isinstance(message, Command):
                self.handle_command(message)

            else:
                raise Exception(f"{message} was not an Event or Command")

    def handle_event(self, event: Event):
        for handler in self._event_handlers[type(event)]:
            handler(event)
            self.queue.extend(self._uow.collect_new_events())

    def handle_command(self, command: Command):
        handler = self._command_handlers[type(command)]
        handler(command)
        self.queue.extend(self._uow.collect_new_events())
