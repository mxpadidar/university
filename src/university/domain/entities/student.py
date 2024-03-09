from datetime import datetime

from backbone.domain.abstract_entity import AbstractEntity


class Student(AbstractEntity):
    id: int
    user_id: int
    registration_date: datetime
