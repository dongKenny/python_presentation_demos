def main():
    fruit_counts = dict()
    fruit_counts["apple"] = 5
    fruit_counts["watermelon"] = 1
    fruit_counts["strawberry"] = 8
    fruit_counts["pineapple"] = 2

    print(fruit_counts)

    # sorted(iterable, key, reverse)
    ascending_sorted_fruit_counts = sorted(fruit_counts.items(), key=lambda fruit: fruit[1])
    descending_sorted_fruit_counts = sorted(fruit_counts.items(), key=lambda fruit: fruit[1], reverse=True)
    print(ascending_sorted_fruit_counts)
    print(descending_sorted_fruit_counts)

    fruit_names = list(fruit_counts.keys())
    fruit_names.sort()

    print(fruit_names)


if __name__ == "__main__":
    main()
