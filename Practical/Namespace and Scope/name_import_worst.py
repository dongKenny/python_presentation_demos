from name_worst import *  # Import * is very bad


def debug_login():
    my_login = {"catdog57": "password1234"}
    print(my_logins.items())


print("Hello World!")
debug_login()
print()
print(f'Globals dict is: {globals()}')
print(f"Logins are: {globals()['my_logins']}")