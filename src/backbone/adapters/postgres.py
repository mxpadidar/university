from sqlalchemy import create_engine
from sqlalchemy.orm import registry, sessionmaker

from backbone.configs import configs

engine = create_engine(configs.POSTGRES_URI)

session_maker = sessionmaker(bind=engine, autocommit=False, autoflush=False)

mapper_registry = registry()
