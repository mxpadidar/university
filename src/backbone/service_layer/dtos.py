from dataclasses import dataclass

from backbone.domain.enums import FileGroup


@dataclass(frozen=True)
class Command: ...


@dataclass(frozen=True)
class Event: ...


@dataclass
class FileDto:
    filename: str
    file_group: FileGroup
    size: int
    content_type: str
