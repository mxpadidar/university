from enum import Enum, auto


class PostgresSchema(Enum):
    UNIVERSITY = "university"
    SHARED = "shared"
    ZVERIFIER = "zverifier"


class FileGroup(Enum):
    USER = auto()


class EntityType(Enum):
    UNIVERSITY = auto()
    FILE = auto()
    USER_FACE = auto()
    COURSE = auto()
