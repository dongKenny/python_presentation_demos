def get_message(message_exists: bool):
    return "Hello World!" if message_exists else None


def get_weather_tuple(is_sunny: bool):
    return ("Rainy", "Sunny")[is_sunny]


def get_weather(is_sunny: bool):
    return "Sunny" if is_sunny else "Rainy"


def main():
    # Sunny if True, Rainy if False
    print(get_weather(True))
    print(get_weather(False))
    print()

    # (Rainy, Sunny)[T/F]
    print(get_weather_tuple(True))
    print(get_weather_tuple(False))
    print()

    # T/F or Default
    message = get_message(True)
    print(message or "No messages found")


if __name__ == "__main__":
    main()
