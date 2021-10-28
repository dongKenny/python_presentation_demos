def squares_demo():
    numbers = [1, 2, 3, 4, 5]
    squares = [num * num for num in numbers]
    odd_squares = [num * num for num in numbers if num % 2 == 1]

    print(numbers)
    print(squares)
    print(odd_squares)
    print()


def matrix_demo():
    matrix = [[0 for _ in range(3)] for _ in range(3)]
    print(matrix)

    flattened_matrix = [value for sublist in matrix for value in sublist]
    print(flattened_matrix)
    print()

    '''
    Equivalent to:
        for sublist in matrix:
            for val in sublist:
                flattened_matrix.append(val)
    '''


def main():
    squares_demo()
    matrix_demo()


if __name__ == "__main__":
    main()
