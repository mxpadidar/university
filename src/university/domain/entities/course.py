from backbone.domain.abstract_entity import AbstractEntity
from backbone.domain.enums import EntityType
from university.domain.enums import CourseModality, CourseType


class Course(AbstractEntity):
    id: int
    university_id: int
    teacher_id: int
    course_number: int
    title: str
    course_type_id: int
    course_modality_id: int
    coefficient: int
    course_group_number_id: int
    events: list

    @classmethod
    def create(
        cls,
        university_id: int,
        teacher_id: int,
        course_number: int,
        title: str,
        course_type: CourseType,
        course_modality: CourseModality,
        course_group_number_id: int,
        coefficient: int,
    ) -> "Course":
        course = cls()
        course.university_id = university_id
        course.teacher_id = teacher_id
        course.course_number = course_number
        course.title = title
        course.course_type_id = course_type.value
        course.course_modality_id = course_modality.value
        course.coefficient = coefficient
        course.course_group_number_id = course_group_number_id
        return course

    @classmethod
    def entity_type(cls) -> EntityType:
        return EntityType.COURSE

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "university_id": self.university_id,
            "teacher_id": self.teacher_id,
            "course_number": self.course_number,
            "title": self.title,
            "course_type_id": self.course_type_id,
            "course_modality_id": self.course_modality_id,
            "coefficient": self.coefficient,
            "course_group_number_id": self.course_group_number_id,
        }
