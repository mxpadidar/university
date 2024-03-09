from backbone.adapters.postgres import mapper_registry
from university.adapters.data_models.course_data_model import course_data_model
from university.domain.entities.course import Course


def start_mapper():
    mapper_registry.map_imperatively(Course, course_data_model)
