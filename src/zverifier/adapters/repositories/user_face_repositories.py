from sqlalchemy.orm import Query

from backbone.adapters.abstract_sqlalchemy_repository import (
    AbstractSqlalchemyRepository,
)
from backbone.domain.abstract_repository import AbstractRepository
from zverifier.domain.entities.user_face import UserFace


class UserFaceRepository(AbstractRepository): ...


class SqlAlchemyUserFaceRepository(AbstractSqlalchemyRepository, UserFaceRepository):

    @property
    def query(self) -> Query:
        return self._session.query(UserFace)
