from enum import Enum, auto


class FileGroup(Enum):
    USER = auto()


class EntityType(Enum):
    FILE = auto()
    USER_FACE = auto()
