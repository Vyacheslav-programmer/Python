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

# Университеты
universities = [
    University(1, "МГТУ"),
    University(2, "МГУ"),
    University(3, "НИУ ВШЭ")
]

# Факультеты
faculties = [
    Faculty(1, "ИУ5", 50000, 1),
    Faculty(2, "МТ4", 45000, 1),
    Faculty(3, "ГУИМЦ", 30000, 2),
    Faculty(4, "ИУ8", 60000, 3),
    Faculty(5, "РК9", 35000, 3)
]

# Связь многие-ко-многим
fac_uni = [
    FacultyUniversity(1, 1),
    FacultyUniversity(2, 1),
    FacultyUniversity(3, 2),
    FacultyUniversity(4, 3),
    FacultyUniversity(5, 3)
]

def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(f.name, f.salary, u.name) 
                   for u in universities 
                   for f in faculties 
                   if f.uni_id == u.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(u.name, fu.university_id, fu.faculty_id)
                         for u in universities
                         for fu in fac_uni 
                         if u.id == fu.university_id]
    
    many_to_many = [(f.name, f.salary, uni_name)
                    for uni_name, uni_id, fac_id in many_to_many_temp
                    for f in faculties if f.id == fac_id]

    # Задание B1: Все факультеты, где название начинается с "И", и их университеты
    print("\nЗадание B1\n")
    res_1 = [(f_name, u_name) for f_name, _, u_name in one_to_many if f_name.startswith("И")]
    print(res_1)

    # Задание B2: Университеты с минимальной зарплатой на каждом факультете, отсортировано по зарплате
    print("\nЗадание B2\n")
    res_2_unsorted = []
    for u in universities:
        u_faculties = list(filter(lambda x: x[2] == u.name, one_to_many))
        if u_faculties:
            min_salary = min(sal for _, sal, _ in u_faculties)
            res_2_unsorted.append((u.name, min_salary))
    res_2 = sorted(res_2_unsorted, key=itemgetter(1))
    print(res_2)

    # Задание B3: Список всех факультетов и университетов, отсортированный по факультетам
    print("\nЗадание B3\n")
    res_3 = sorted(many_to_many, key=itemgetter(0))
    print(res_3)

if __name__ == "__main__":
    main()



# Результаты выполнения:

# Задание B1

# [('ИУ5', 'МГТУ'), ('ИУ8', 'НИУ ВШЭ')]

# Задание B2

# [('МГУ', 30000), ('НИУ ВШЭ', 35000), ('МГТУ', 45000)]

# Задание B3

# [('ГУИМЦ', 30000, 'МГУ'), ('ИУ5', 50000, 'МГТУ'), ('ИУ8', 60000, 'НИУ ВШЭ'), ('МТ4', 45000, 'МГТУ'), ('РК9', 35000, 'НИУ ВШЭ')]