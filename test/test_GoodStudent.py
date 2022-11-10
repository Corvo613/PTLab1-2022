from src.Types import DataType
from src.GoodStudent import GoodStudent


class TestGoodStudent:
    def test_with_no_students(self):
        data: DataType = {}
        student = GoodStudent(data)
        assert student.calc() == "Нет студентов с 76 баллами минимум по трем предметам"

    def test_with_bad_students(self):
        data: DataType = {
            "Петров Петр Игоревич":
                [
                    ("математика", 61),
                    ("химия", 75),
                    ("физика", 70)
                ],

            "Редько Игорь Алексеевич":
                [
                    ("математика", 70),
                    ("химия", 90),
                    ("информатика", 61)
                ],
        }

        student = GoodStudent(data)
        assert student.calc() == "Нет студентов с 76 баллами минимум по трем предметам"

    def test_with_few_subjects(self):
        data: DataType = {
            "Петров Петр Игоревич":
                [
                    ("математика", 100),
                    ("химия", 90),
                ],

            "Редько Игорь Алексеевич":
                [
                    ("математика", 90),
                    ("химия", 85)
                ]
        }

        student = GoodStudent(data)
        assert student.calc() == "Нет студентов с 76 баллами минимум по трем предметам"

    def test_with_one_good_stedent(self):
        data: DataType = {
            "Петров Петр Игоревич":
                [
                    ("математика", 61),
                    ("химия", 75),
                    ("физика", 70)
                ],

            "Редько Игорь Алексеевич":
                [
                    ("математика", 70),
                    ("химия", 90),
                    ("информатика", 61)
                ],
            "Антонов Иван Андреевич":
                [
                    ("математика", 78),
                    ("химия", 90),
                    ("информатика", 88)
                ]
        }

        student = GoodStudent(data)
        assert student.calc() == "Антонов Иван Андреевич"

    def test_with_several_good_students(self):
        data: DataType = {
            "Петров Петр Игоревич":
                [
                    ("математика", 80),
                    ("химия", 99),
                    ("физика", 100)
                ],

            "Редько Игорь Алексеевич":
                [
                    ("математика", 70),
                    ("химия", 90),
                    ("информатика", 61)
                ],
            "Антонов Иван Андреевич":
                [
                    ("математика", 78),
                    ("химия", 90),
                    ("информатика", 88)
                ]
        }

        student = GoodStudent(data)
        assert student.calc() in ["Петров Петр Игоревич", "Антонов Иван Андреевич"]
