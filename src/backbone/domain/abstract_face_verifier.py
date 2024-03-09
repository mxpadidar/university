from abc import ABC, abstractmethod

from backbone.service_layer.dtos import FileDto


class AbstractFaceVerifier(ABC):
    @abstractmethod
    def register_user_face(self, user_id: int, face_image_data: FileDto) -> dict: ...

    @abstractmethod
    def verify_user_face(self, user_id: int, face_image_data: FileDto) -> bool: ...
