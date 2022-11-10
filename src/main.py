# -*- coding: utf-8 -*-
import argparse
import sys

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from YAMLDataReader import YAMLDataReader
from GoodStudent import GoodStudent


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    if path.split('.')[-1] == 'txt':
        reader = TextDataReader()
    elif path.split('.')[-1] == 'yml':
        reader = YAMLDataReader()
    else:
        print("Данный формат файла не поддерживается или файл не существует")
        return

    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    student = GoodStudent(students).calc()
    print("Good student:", student)


if __name__ == "__main__":
    main()
