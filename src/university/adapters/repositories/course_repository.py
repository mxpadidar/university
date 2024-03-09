from sqlalchemy.orm import Query

from backbone.adapters.abstract_sqlalchemy_repository import (
    AbstractSqlalchemyRepository,
)
from backbone.domain.abstract_repository import AbstractRepository
from university.domain.entities.course import Course


class CourseRepository(AbstractRepository): ...


class SqlalchemyCourseRepository(AbstractSqlalchemyRepository, CourseRepository):
    @property
    def query(self) -> Query:
        return self._session.query(Course)
