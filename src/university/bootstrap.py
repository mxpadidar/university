from backbone.service_layer.message_bus import MessageBus
from backbone.service_layer.utils import inject_dependencies
from university.adapters.mappers import start_mapper
from university.service_layer.command_handlers import command_handlers
from university.service_layer.event_handlers import event_handlers
from university.service_layer.unit_of_work import (
    UniversityAbstractUnitOfWork,
    UniversitySqlalchemyUnitOfWork,
)


def bootstrap(
    start_orm: bool = True,
    uow: UniversityAbstractUnitOfWork = UniversitySqlalchemyUnitOfWork(),
) -> MessageBus:

    if start_orm:
        start_mapper()

    deps = {"uow": uow}
    injected_event_handlers = {
        event_type: [inject_dependencies(handler, deps) for handler in event_handlers]
        for event_type, event_handlers in event_handlers.items()
    }
    injected_command_handlers = {
        command_type: inject_dependencies(handler, deps)
        for command_type, handler in command_handlers.items()
    }

    return MessageBus(
        uow=uow,
        event_handlers=injected_event_handlers,
        command_handlers=injected_command_handlers,
    )
