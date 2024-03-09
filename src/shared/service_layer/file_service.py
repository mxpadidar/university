from backbone.domain.abstract_file_service import AbstractFileService
from backbone.domain.enums import FileGroup
from backbone.service_layer.dtos import FileDto
from shared.adapters.minio_client import MinioClient
from shared.domain.abstract_s3_client import AbstractS3Client
from shared.domain.entities.file import File
from shared.service_layer.unit_of_work import AbstractUnitOfWork, SqlalchemyUnitOfWork


class FileService(AbstractFileService):
    def __init__(
        self,
        client: AbstractS3Client = MinioClient(),
        uow: AbstractUnitOfWork = SqlalchemyUnitOfWork(),
    ) -> None:
        self._client = client
        self._uow = uow
        self._uploaded_files: list[FileDto] = list()

    def get(self, file_id: int) -> bytes:
        with self._uow as uow:
            file: File | None = uow.file.get_by_id(file_id)
            if not file:
                raise ValueError
            file_group: FileGroup | None = None

            for group in FileGroup.__members__.values():
                if file.file_group_id == group.value:
                    file_group = group
                    break

            if not file_group:
                raise ValueError

            return self._client.download(file_group=file_group, filename=file.filename)

    def post(self, file_data: FileDto, file_content: bytes) -> dict:
        try:
            file_path = self._client.upload(file_data, file_content)
            self._uploaded_files.append(file_data)
            file = File.create(
                filename=file_data.filename,
                group=file_data.file_group,
                path=file_path,
                size=file_data.size,
                content_type=file_data.content_type,
            )
            with self._uow as uow:
                uow.file.add(file)
                uow.commit()
                return file.to_dict()

        except Exception:
            self.rollback()
            raise

    def rollback(self) -> None:
        for file in self._uploaded_files:
            self._client.delete(file)
