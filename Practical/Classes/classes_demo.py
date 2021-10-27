from Practical.Classes.student import Student


def student_demonstration(first_grade: float, second_grade: float):
    first_student = Student("Kenny", "Dong")
    second_student = Student("Hammond", "Cheese")

    first_student.grade = first_grade
    second_student.grade = second_grade

    print(f"{first_student}'s grade is {first_student.grade:.2f}")
    print(second_student.__repr__())


def main():
    student_demonstration(99.4, 2)


if __name__ == "__main__":
    main()
