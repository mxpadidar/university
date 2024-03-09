from datetime import datetime

from backbone.domain.abstract_entity import AbstractEntity


class CourseTime(AbstractEntity):
    id: int
    course_id: int
    classroom_id: int
    start_at: datetime
    end_at: datetime
    day_of_week: str
