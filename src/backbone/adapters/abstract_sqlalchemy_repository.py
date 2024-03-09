from abc import abstractmethod

from sqlalchemy.orm import Query, Session

from backbone.domain.abstract_repository import AbstractRepository


class AbstractSqlalchemyRepository(AbstractRepository):

    def __init__(self, session: Session) -> None:
        super().__init__()
        self._session = session

    @property
    @abstractmethod
    def query(self) -> Query: ...

    def _add(self, entity):
        self._session.add(entity)

    def _get_by_id(self, id: int):
        return self.query.filter_by(id=id).one_or_none()
