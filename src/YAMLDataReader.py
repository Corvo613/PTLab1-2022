from Types import DataType
from DataReader import DataReader
import yaml

class YAMLDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.studentss: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:

#TODO доделать