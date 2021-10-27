from person import Person


class Student(Person):
    # Class Variable
    school = "University of San Francisco"
    classes = []

    def __init__(self, first_name: str = "", last_name: str = ""):
        super().__init__(first_name, last_name)
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if value != float(value):
            raise TypeError("grade must be a numeric")
        if 0. <= value <= 100:
            self._grade = float(value)
        else:
            raise ValueError("grade must be between 0 and 100")

    def print_table(self):
        print(f'{self.first_name: ^10}|{self.last_name: ^10}|{self.grade: ^10.02f}')

    def __repr__(self):
        return f'Student({self.first_name!r}, {self.last_name!r}, {self.grade:.2f})'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
