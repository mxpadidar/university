from abc import ABC, abstractmethod

from backbone.service_layer.dtos import FileDto


class AbstractFileService(ABC):

    @abstractmethod
    def get(self, file_id: int) -> FileDto:
        pass

    @abstractmethod
    def post(self, file_data: FileDto, file_content: bytes) -> dict:
        pass
