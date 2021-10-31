def set_excitement(message: str, optional_punctuation: str = None):
    optional_punctuation = optional_punctuation or "."
    return f"{message}{optional_punctuation}"


def get_weather(is_sunny: bool):
    return "Sunny" if is_sunny else "Rainy"


def main():
    # Sunny if True, Rainy if False
    print(get_weather(True))
    print(get_weather(False))
    print()

    # T/F or Default
    message = set_excitement("Hello, World")
    print(message)

    message_but_happy = set_excitement("Hello, World", "!!!")
    print(message_but_happy)


if __name__ == "__main__":
    main()
