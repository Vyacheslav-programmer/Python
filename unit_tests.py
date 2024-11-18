import unittest
from main import create_one_to_many, create_many_to_many, task_b1, task_b2, task_b3, Faculty, University, FacultyUniversity


class TestMainMethods(unittest.TestCase):
    def setUp(self):
        self.universities = [
            University(1, "МГТУ"),
            University(2, "МГУ"),
            University(3, "НИУ ВШЭ")
        ]

        self.faculties = [
            Faculty(1, "ИУ5", 50000, 1),
            Faculty(2, "МТ4", 45000, 1),
            Faculty(3, "ГУИМЦ", 30000, 2),
            Faculty(4, "ИУ8", 60000, 3),
            Faculty(5, "РК9", 35000, 3)
        ]

        self.fac_uni = [
            FacultyUniversity(1, 1),
            FacultyUniversity(2, 1),
            FacultyUniversity(3, 2),
            FacultyUniversity(4, 3),
            FacultyUniversity(5, 3)
        ]

        self.one_to_many = create_one_to_many(self.faculties, self.universities)
        self.many_to_many = create_many_to_many(self.faculties, self.universities, self.fac_uni)

    def test_task_b1(self):
        result = task_b1(self.one_to_many)
        reference = [('ИУ5', 'МГТУ'), ('ИУ8', 'НИУ ВШЭ')]
        self.assertEqual(result, reference)

    def test_task_b2(self):
        result = task_b2(self.one_to_many, self.universities)
        reference = [('МГУ', 30000), ('НИУ ВШЭ', 35000), ('МГТУ', 45000)]
        self.assertEqual(result, reference)

    def test_task_b3(self):
        result = task_b3(self.many_to_many)
        reference = [
            ('ГУИМЦ', 30000, 'МГУ'),
            ('ИУ5', 50000, 'МГТУ'),
            ('ИУ8', 60000, 'НИУ ВШЭ'),
            ('МТ4', 45000, 'МГТУ'),
            ('РК9', 35000, 'НИУ ВШЭ')
        ]
        self.assertEqual(result, reference)


if __name__ == '__main__':
    unittest.main()
