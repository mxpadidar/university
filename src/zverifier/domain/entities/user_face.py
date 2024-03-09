from datetime import datetime

from backbone.domain.abstract_entity import AbstractEntity
from backbone.domain.enums import EntityType


class UserFace(AbstractEntity):
    id: int
    user_id: int
    face_file_id: int
    created_at: datetime
    updated_at: datetime | None
    deleted_at: datetime | None

    @classmethod
    def create(cls, user_id: int, face_file_id: int) -> "UserFace":
        user_face = cls()
        user_face.user_id = user_id
        user_face.face_file_id = face_file_id
        user_face.created_at = datetime.utcnow()
        return user_face

    @classmethod
    def entity_type(cls) -> EntityType:
        return EntityType.USER_FACE

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "face_file_id": self.face_file_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
        }
