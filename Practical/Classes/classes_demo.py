from student import Student


def class_variable_demo(first_student: Student, second_student: Student):
    print(f'{first_student} goes to {first_student.school}')
    print(f'{second_student} goes to {first_student.school}')
    print()

    first_student.classes.extend(["Intermediate Japanese I", "Operating Systems"])
    second_student.classes.extend(["Underwater Basket Weaving", "Operating Systems in Python"])

    print(f'{first_student}\'s classes are {first_student.classes}')
    print(f'{second_student}\'s classes are {second_student.classes}')


def grade_demo(first_student: Student, second_student: Student, first_grade: float, second_grade: float):
    first_student.grade = first_grade
    second_student.grade = second_grade

    first_student.print_table()
    second_student.print_table()
    print()


def main():
    first_student = Student("Kenny", "Dong")
    second_student = Student("Hammond", "Cheese")

    grade_demo(first_student, second_student, 99.4, 2)
    class_variable_demo(first_student, second_student)


if __name__ == "__main__":
    main()
