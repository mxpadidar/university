from backbone.adapters.postgres import mapper_registry
from shared.adapters.data_models.file_data_model import file_data_model
from shared.domain.entities.file import File

mapper_registry.map_imperatively(File, file_data_model)
