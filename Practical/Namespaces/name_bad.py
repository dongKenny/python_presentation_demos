def debug_logins():
    print(my_logins.items())


def factorial(x):
    result = 1
    for i in range(x, 0, -1):
        # Oopsies! We accidentally made it calculate j**x
        result *= j

    return result


# It's a script, we should run it!
j = 3
if __name__ == "__main__":
    my_logins = {"bigcheese23": "hunter2"}
    debug_logins()

    j = 4
    print(factorial(j))
