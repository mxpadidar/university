from sqlalchemy.orm import Query

from backbone.adapters.abstract_sqlalchemy_repository import (
    AbstractSqlalchemyRepository,
)
from backbone.domain.abstract_repository import AbstractRepository
from shared.domain.entities.file import File


class FileRepository(AbstractRepository): ...


class SqlAlchemyFileRepository(AbstractSqlalchemyRepository, FileRepository):

    @property
    def query(self) -> Query:
        return self._session.query(File)
