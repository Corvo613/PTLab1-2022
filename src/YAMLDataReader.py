from Types import DataType
from DataReader import DataReader
import yaml


class YAMLDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as stream:
            file = yaml.safe_load(stream)
            for name in file:
                self.key = name
                self.students[self.key] = []
                for pair in dict.items(file[name]):
                    self.students[self.key].append(pair)
        return self.students
