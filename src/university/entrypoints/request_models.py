from pydantic import BaseModel

from university.domain.enums import CourseModality, CourseType


class CreateCourseRequest(BaseModel):
    teacher_id: int
    course_number: int
    title: str
    course_type: CourseType
    course_modality: CourseModality
    course_group_number_id: int
    coefficient: int
