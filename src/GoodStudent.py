# -*- coding: utf-8 -*-
from Types import DataType
from random import choice

class GoodStudent():
    def __init__(self, data : DataType) -> None:
        self.data = data
        self.students : list[str] = []

    def calc(self) -> str:
        for student in self.data:
            if len(self.data[student]) < 3:
                continue
            goodGrades = 0
            for subject in self.data[student]:
                if subject[1] >= 76:
                    goodGrades += 1
            if goodGrades >= 3:
                self.students.append(student)
        if self.students:
            return choice(self.students)
        else:
            return "Нет студентов с 76 баллами минимум по трем предметам"