from typing import List
from Classes.book_dataclass import Book


def if_elif_demo(command: str):
    commands = command.split()
    if len(commands) > 1 and commands[0] == "go" and commands[1] in ["north", "south", "east", "west"]:
        print(f"Going {commands[1]}")
    elif len(commands) == 1 and commands[0] in ["north", "south", "east", "west"]:
        print(f"Going {commands[0]}")
    elif len(commands) > 1 and commands[0] == "get":
        print(f"Picked up {commands[1]}")
    elif len(commands) > 2 and commands[0] == "pick":
        if commands[1] == "up":
            print(f"Picked up {commands[2]}")
        elif commands[2] == "up":
            print(f"Picked up {commands[1]}")
    elif len(commands) > 1 and commands[0] == "say":
        print(f"Said \"{' '.join(commands[1:])}\"")
    else:
        print("Unknown command given")


def match_case_demo(command: str):
    match command.split():
        # Captures the value after 'go' as direction if it is a cardinal direction
        case ["go", ("north" | "south" | "east" | "west") as direction] | [("north" | "south" | "east" | "west") as direction]:
            print(f'Going {direction}')
        case ["get", item] | ["pick", "up", item] | ["pick", item, "up"]:
            print(f"Picked up {item}")
        case ["say", *words]:
            print(f"Said \"{' '.join(words)}\"")
        case _:
            print("Unknown command given")


def match_case_demo_guard(command: str, directions: List[str]):
    match command.split():
        # Binds the value after 'go' to the direction if it is a cardinal direction
        case ["go", direction] if direction in directions:
            print(f'Going {direction}')
        case ["go", invalid]:
            print(f'Cannot go "{invalid}"')
        case ["get", item] | ["pick", "up", item] | ["pick", item, "up"]:
            print(f"Picked up {item}")
        case ["say", *words]:
            print(f"Said \"{' '.join(words)}\"")
        case _:
            print("Unknown command given")


def match_case_class_demo(book: Book):
    match book:
        case Book("To Kill a Mockingbird", 1960, "Harper Lee"):
            print("That's a good book!")
        case Book("C Programming Language, 2nd Edition", 1978):
            print("That's a... book!")
        case Book(year=1867):
            print("That's a book from 1867, how specific!")
        case Book():
            print("I would've appreciated a recommendation, but thanks I guess?")


def main():
    if_elif_demo("go south")
    if_elif_demo("pick up sword")
    if_elif_demo("pick bow up")
    if_elif_demo("get staff")
    if_elif_demo("say Huzzah World!")
    if_elif_demo("north")
    print()

    match_case_demo("go south")
    match_case_demo("pick up sword")
    match_case_demo("pick bow up")
    match_case_demo("get staff")
    match_case_demo("say Huzzah World!")
    match_case_demo("north")
    print()

    match_case_demo_guard("go south", ["south"])
    match_case_demo_guard("go south", ["north"])
    print()

    tkam = Book("To Kill a Mockingbird", 1960, "Harper Lee")
    c_book = Book("C Programming Language, 2nd Edition", 1978)
    old_book = Book("War and Peace", 1867, "Leo Tolstoy")
    book = Book()

    match_case_class_demo(tkam)
    match_case_class_demo(c_book)
    match_case_class_demo(old_book)
    match_case_class_demo(book)


if __name__ == "__main__":
    main()
