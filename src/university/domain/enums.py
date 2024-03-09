from enum import Enum, auto


class CourseType(Enum):
    THEORY = auto()
    LAB = auto()


class CourseModality(Enum):
    ONLINE = auto()
    OFFLINE = auto()
