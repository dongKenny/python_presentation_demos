from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name

    @abstractmethod
    def print_table(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass
