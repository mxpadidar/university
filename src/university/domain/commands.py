from dataclasses import dataclass

from backbone.service_layer.dtos import Command
from university.domain.enums import CourseModality, CourseType


@dataclass(frozen=True)
class CreateCourseCommand(Command):
    university_id: int
    teacher_id: int
    course_group_number_id: int
    course_number: int
    title: str
    course_type: CourseType
    course_modality: CourseModality
    coefficient: int
