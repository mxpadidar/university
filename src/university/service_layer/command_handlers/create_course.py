from university.domain.commands import CreateCourseCommand
from university.domain.entities.course import Course
from university.domain.events import CourseCreatedEvent
from university.service_layer.unit_of_work import UniversityAbstractUnitOfWork


def create_course_handler(
    command: CreateCourseCommand, uow: UniversityAbstractUnitOfWork
):
    course = Course.create(
        university_id=command.university_id,
        teacher_id=command.teacher_id,
        course_number=command.course_number,
        title=command.title,
        course_type=command.course_type,
        course_modality=command.course_modality,
        course_group_number_id=command.course_group_number_id,
        coefficient=command.coefficient,
    )
    course.events.append(CourseCreatedEvent(event_title=course.title))
    with uow:
        uow.courses.add(course)
        uow.commit()

    return course.to_dict()
