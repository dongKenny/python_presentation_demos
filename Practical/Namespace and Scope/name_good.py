def debug_logins():
    print(f"Debug logins called from {__name__}")
    my_logins = {"mmalensek@usfca.edu": "purplelaces1957", "cheesecakeoverlord94": "cat123"}
    print(list(my_logins.items()))


def factorial(num):
    result = 1

    def factorial_loop():
        nonlocal result
        result = 1

        for i in range(num, 0, -1):
            result *= i

    factorial_loop()

    return result


def main():
    my_logins = {"bigcheese23": "hunter2"}
    debug_logins()
    print(f'factorial of 5 is {factorial(5)}')


# It's a script, we should run it!
if __name__ == "__main__":
    main()
