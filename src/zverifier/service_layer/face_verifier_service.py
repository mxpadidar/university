from backbone.domain.abstract_face_verifier import AbstractFaceVerifier
from backbone.domain.abstract_file_service import AbstractFileService
from backbone.service_layer.dtos import FileDto
from shared.service_layer.file_service import FileService
from zverifier.domain.entities.user_face import UserFace
from zverifier.service_layer.unit_of_work import (
    AbstractUnitOfWork,
    SqlalchemyUnitOfWork,
)


class FaceVerifierService(AbstractFaceVerifier):
    def __init__(
        self,
        file_service: AbstractFileService = FileService(),
        uow: AbstractUnitOfWork = SqlalchemyUnitOfWork(),
    ) -> None:
        self._file_service = file_service
        self._uow = uow

    def register_user_face(
        self, user_id: int, image_data: FileDto, image_content: bytes
    ) -> dict:
        face_image = self._file_service.post(
            file_data=image_data, file_content=image_content
        )
        user_face = UserFace.create(user_id=user_id, face_file_id=face_image["id"])

        with self._uow as uow:
            uow.user_face.add(user_face)
            uow.commit()
            return user_face.to_dict()

    def verify_user_face(self, user_id: int, image_content: bytes) -> bool:
        with self._uow as uow:
            user_face: UserFace = uow.user_face.get_by_id(id=user_id)
            if not user_face:
                raise ValueError

            # face_image = self._file_service.get(file_id=user_face.face_file_id)

            # TODO:  implement face verification logic

            return True
