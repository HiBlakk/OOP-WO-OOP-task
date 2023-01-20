from .student import create_student
from .utils import validate_data


def create_aspirant_struct(name, group, average_grade):
    if validate_data(name, group, average_grade):
        return create_student(name, group, average_grade) | {
            'degree': 'aspirant'
        }
    else:
        raise ValueError
