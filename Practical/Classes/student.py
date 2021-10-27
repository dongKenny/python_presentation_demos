class Person(object):
    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name

    def print_table(self):
        pass

    def __repr__(self):
        pass


class Student(Person):
    def __init__(self, first_name: str = "", last_name: str = ""):
        super().__init__(first_name, last_name)
        self.__grade = 0

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        if value != float(value):
            raise TypeError("grade must be a numeric")
        if 0. <= value <= 100:
            self.__grade = float(value)
        else:
            raise ValueError("grade must be between 0 and 100")

    def __repr__(self):
        return f'Student({self.first_name!r}, {self.last_name!r}, {self.__grade:.2f})'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
