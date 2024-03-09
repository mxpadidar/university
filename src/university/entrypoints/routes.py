from fastapi import APIRouter, Depends

from backbone.adapters.dependencies import get_current_user_info
from backbone.service_layer.dtos import UserDto
from university.bootstrap import bootstrap
from university.domain.commands import CreateCourseCommand
from university.entrypoints.request_models import CreateCourseRequest

bus = bootstrap()

router = APIRouter(prefix="/university", tags=["university"])


@router.post("/course")
async def create_course(
    rm: CreateCourseRequest, user_info: UserDto = Depends(get_current_user_info)
):
    command = CreateCourseCommand(
        university_id=user_info.university_id,
        teacher_id=rm.teacher_id,
        course_group_number_id=rm.course_group_number_id,
        course_number=rm.course_number,
        title=rm.title,
        course_type=rm.course_type,
        course_modality=rm.course_modality,
        coefficient=rm.coefficient,
    )

    return bus.handle(command)
