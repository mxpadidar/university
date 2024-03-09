from sqlalchemy import Column, Integer, String, Table

from backbone.adapters.postgres import mapper_registry

file_data_model = Table(
    "files",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("filename", String),
    Column("path", String),
)
