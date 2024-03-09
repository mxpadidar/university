from university.domain.events import CourseCreatedEvent


def course_created_handler(event: CourseCreatedEvent):
    print(f"Course created: {event.event_title}")
