def get_aspirant_grant(aspirant):
    if aspirant.get('degree') != 'aspirant':
        raise ValueError
    
    return _get_grant(aspirant.get('average_grade', 0), 3500, 4500, 5000)


def get_bachelor_grant(bachelor):
    if bachelor.get('degree') != 'bachelor':
        raise ValueError
    
    return _get_grant(bachelor.get('average_grade', 0), 1500, 2000, 3000)


def _get_grant(grade, minimal, usual, maximal):
    if grade == 5:
        return maximal
    elif 4 <= grade < 5:
        return usual
    elif 3 <= grade < 4:
        return minimal
    else:
        return 0


def update_average_grade(student, average_grade):
    if not 0 <= average_grade <= 5:
        raise ValueError
    student['average_grade'] = average_grade
    return student


def validate_data(name, group, average_grade):
    return isinstance(name, str) and isinstance(group, (int, str)) and isinstance(average_grade, (int, float)) and 0 <= average_grade <= 5
