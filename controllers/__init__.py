from . import Discipline
from . import Course
from . import Student
from . import Professor

routes = [
    Discipline.router,
    Course.router,
    Student.router,
    Professor.router
]
