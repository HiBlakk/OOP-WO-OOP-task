from .bachelor import create_bachelor_struct
from .aspirant import create_aspirant_struct
from .utils import update_average_grade, get_aspirant_grant, get_bachelor_grant


def test():
    bachelor = create_bachelor_struct('Petya', '1011', 4.3)
    aspirant = create_aspirant_struct('Georgiy', '1020', 5)
    print(bachelor, get_bachelor_grant(bachelor))
    print(aspirant, get_aspirant_grant(aspirant))
    bachelor = update_average_grade(bachelor, 5)
    aspirant = update_average_grade(aspirant, 3)
    print(bachelor, get_bachelor_grant(bachelor))
    print(aspirant, get_aspirant_grant(aspirant))


if __name__ == '__main__':
    test()
