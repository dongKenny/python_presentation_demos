def match_case_demo(command: str):
    match command.split():
        case ["go", ("north" | "south" | "east" | "west") as direction]:
            print(f'Going {direction}')
        case ["get", item] | ["pick", "up", item] | ["pick", item, "up"]:
            print(f"Picked up {item}")


def main():
    match_case_demo("go south")
    match_case_demo("pick up sword")
    match_case_demo("pick bow up")
    match_case_demo("get staff")


if __name__ == "__main__":
    main()
