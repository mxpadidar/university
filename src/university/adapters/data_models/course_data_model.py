from sqlalchemy import Column, Integer, String, Table

from backbone.adapters.postgres import mapper_registry
from backbone.domain.enums import PostgresSchema

course_data_model = Table(
    "course",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String),
    Column("university_id", Integer),
    Column("teacher_id", Integer),
    Column("course_group_number_id", Integer),
    Column("course_number", Integer),
    Column("course_type_id", Integer),
    Column("course_modality_id", Integer),
    Column("coefficient", Integer),
    schema=PostgresSchema.UNIVERSITY.value,
)
