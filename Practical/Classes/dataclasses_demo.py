from book_dataclass import Book
from dataclasses import astuple, asdict


def main():
    tkam = Book("To Kill a Mockingbird", 1960, "Harper Lee")
    print(tkam)
    print(astuple(tkam))    # Converts to tuple
    print(asdict(tkam))     # Converts to dict
    print()
    # tkam.title = "The Very Hungry Caterpillar"

    default = Book()
    print(default)


if __name__ == "__main__":
    main()
