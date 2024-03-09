from io import BytesIO

from minio import Minio
from minio.error import S3Error

from backbone.configs import configs
from backbone.domain.enums import FileGroup
from backbone.service_layer.dtos import FileDto
from shared.domain.abstract_s3_client import AbstractS3Client


class FileUploadError(Exception): ...


class FileDeleteError(Exception): ...


class MinioClient(AbstractS3Client):
    def __init__(
        self,
        host: str = configs.MINIO_HOST,
        port: int = configs.MINIO_PORT,
        access_key: str = configs.MINIO_ACCESS_KEY,
        secret_key: str = configs.MINIO_SECRET_KEY,
    ) -> None:
        self.client = Minio(
            endpoint=f"{host}:{port}",
            access_key=access_key,
            secret_key=secret_key,
            secure=False,
        )

    def upload(self, data: FileDto, file: bytes) -> str:
        try:
            filename = self._generate_unique_filename(data.filename)
            result = self.client.put_object(
                bucket_name=data.file_group.name,
                object_name=filename,
                data=BytesIO(file),
                length=data.size,
                content_type=data.content_type,
            )

            print(result.object_name)
            print(result.version_id)
            return result.object_name
        except S3Error:
            raise FileUploadError

    def download(self, file_group: FileGroup, filename: str) -> bytes:
        try:
            return self.client.get_object(
                bucket_name=file_group.name,
                object_name=filename,
            ).read()
        except S3Error:
            raise FileNotFoundError

    def delete(self, file: FileDto) -> None:
        try:
            self.client.remove_object(
                bucket_name=file.file_group.name,
                object_name=file.filename,
            )
        except S3Error:
            raise FileDeleteError

    def close(self) -> None: ...

    def _generate_unique_filename(self, filename: str) -> str:
        return filename
