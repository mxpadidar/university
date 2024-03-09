from sqlalchemy import create_engine
from sqlalchemy.orm import registry, sessionmaker

from backbone.configs import configs

engine = create_engine(configs.POSTGRES_URI)

session_maker = sessionmaker(bind=engine, autocommit=False, autoflush=False)

mapper_registry = registry()


def create_schemas():
    from sqlalchemy.schema import CreateSchema

    from backbone.domain.enums import PostgresSchema

    session = session_maker()

    for schema in PostgresSchema:
        session.execute(
            CreateSchema(
                name=schema.value,
                if_not_exists=True,
            )
        )

    session.commit()
    session.close()


def create_tables():

    mapper_registry.metadata.create_all(engine, checkfirst=True)
