from name_good import debug_logins  # , factorial


def main():
    print(f"__name__: {__name__}")
    debug_logins()

    print()
    print(f'Globals dict is: {globals()}')
    print(f"Value of 'debug_logins' in globals() is {globals()['debug_logins']}")
    # print(f"Value of 'factorial' in globals() is {globals()['factorial']}")
    # five_factorial = factorial(5)


if __name__ == "__main__":
    main()
