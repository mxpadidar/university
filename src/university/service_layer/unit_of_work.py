from __future__ import annotations

from backbone.adapters.postgres import session_maker
from backbone.domain.abstract_repository import AbstractRepository
from backbone.domain.abstract_unit_of_work import AbstractUnitOfWork
from university.adapters.repositories.course_repository import (
    CourseRepository,
    SqlalchemyCourseRepository,
)


class UniversityAbstractUnitOfWork(AbstractUnitOfWork):
    repositories: set[AbstractRepository]
    courses: CourseRepository


class UniversitySqlalchemyUnitOfWork(UniversityAbstractUnitOfWork):
    def __init__(self, session_maker=session_maker) -> None:
        self._session_maker = session_maker
        self.repositories = set()

    def __enter__(self):
        self._session = self._session_maker()
        self.courses = SqlalchemyCourseRepository(self._session)
        self.repositories.add(self.courses)
        return super().__enter__()

    def _commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()
