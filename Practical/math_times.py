import timeit
import numpy as np


def for_loop_sum(n=100_000_000):
    result = 0
    for i in range(n+1):
        result += i
    return result


def while_loop_sum(n=100_000_000):
    result = 0
    i = 0

    while i <= n:
        result += i
        i += 1

    return result


def sum_sum(n=100_000_000):
    return sum(range(n+1))


def numpy_sum(n=100_000_000):
    return np.sum(np.arange(n+1))


def gauss_sum(n=100_000_000):
    return (n * (n+1)) // 2


def main():
    # All of these calculate the sum of every number up to n and including n
    # e.g. n=100 --> 5050

    print(f"While Loop Sum Time: {timeit.timeit(while_loop_sum, number=1)}")
    print(f"For Loop Sum Time: {timeit.timeit(for_loop_sum, number=1)}")
    print(f"Python Sum Time: {timeit.timeit(sum_sum, number=1)}")
    print(f"Numpy Sum Time: {timeit.timeit(numpy_sum, number=1)}")
    print(f"Gauss Sum Time: {timeit.timeit(gauss_sum, number=1)}")


if __name__ == "__main__":
    main()
