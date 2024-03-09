from __future__ import annotations

from abc import ABC, abstractmethod

from backbone.domain.enums import FileGroup
from backbone.service_layer.dtos import FileDto


class AbstractS3Client(ABC):

    @abstractmethod
    def upload(self, data: FileDto, file: bytes) -> str: ...

    @abstractmethod
    def download(self, file_group: FileGroup, filename: str) -> bytes: ...

    @abstractmethod
    def delete(self, file: FileDto) -> None: ...

    @abstractmethod
    def close(self) -> None: ...
