from __future__ import annotations

from datetime import datetime

from backbone.domain.abstract_entity import AbstractEntity
from backbone.domain.enums import EntityType, FileGroup


class File(AbstractEntity):
    id: int
    filename: str
    file_group_id: int
    path: str
    size: int
    content_type: str
    create_at: datetime
    update_at: datetime | None
    deleted_at: datetime | None

    @classmethod
    def create(
        cls, filename: str, group: FileGroup, path: str, size: int, content_type: str
    ) -> File:
        file = File()
        file.filename = filename
        file.file_group_id = group.value
        file.path = path
        file.size = size
        file.content_type = content_type
        file.create_at = datetime.utcnow()
        return file

    @classmethod
    def entity_type(cls) -> EntityType:
        return EntityType.FILE

    def to_dict(self):
        return {
            "id": self.id,
            "filename": self.filename,
            "file_group_id": self.file_group_id,
            "path": self.path,
            "size": self.size,
            "content_type": self.content_type,
            "create_at": self.create_at,
            "update_at": self.update_at,
            "deleted_at": self.deleted_at,
        }
