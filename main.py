from operator import itemgetter


class Faculty:
    """Факультет"""
    def __init__(self, id, name, salary, uni_id):
        self.id = id
        self.name = name
        self.salary = salary
        self.uni_id = uni_id


class University:
    """Университет"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class FacultyUniversity:
    """Факультеты университетов для связи многие-ко-многим"""
    def __init__(self, faculty_id, university_id):
        self.faculty_id = faculty_id
        self.university_id = university_id


def task_b1(one_to_many):
    """Все факультеты, где название начинается с 'И', и их университеты"""
    return [(f_name, u_name) for f_name, _, u_name in one_to_many if f_name.startswith("И")]


def task_b2(one_to_many, universities):
    """Университеты с минимальной зарплатой на каждом факультете"""
    res = []
    for u in universities:
        u_faculties = list(filter(lambda x: x[2] == u.name, one_to_many))
        if u_faculties:
            min_salary = min(sal for _, sal, _ in u_faculties)
            res.append((u.name, min_salary))
    return sorted(res, key=itemgetter(1))


def task_b3(many_to_many):
    """Список всех факультетов и университетов, отсортированный по факультетам"""
    return sorted(many_to_many, key=itemgetter(0))


def create_one_to_many(faculties, universities):
    return [(f.name, f.salary, u.name)
            for u in universities
            for f in faculties
            if f.uni_id == u.id]


def create_many_to_many(faculties, universities, fac_uni):
    many_to_many_temp = [(u.name, fu.university_id, fu.faculty_id)
                         for u in universities
                         for fu in fac_uni
                         if u.id == fu.university_id]
    return [(f.name, f.salary, uni_name)
            for uni_name, _, fac_id in many_to_many_temp
            for f in faculties if f.id == fac_id]
