from name_bad import *  # Import * is very bad


def factorial(x):
    result = 1
    for i in range(x, 0, -1):
        # Oopsies! We accidentally made it calculate j**x
        result *= j

    return result


def main():
    print(factorial(4))


if __name__ == "__main__":
    main()
