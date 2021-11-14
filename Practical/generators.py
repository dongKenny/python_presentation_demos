import time
import memory_profiler as mem_profile


def get_square_nums_list(n: int = 100_000_000):
    return [i**2 for i in range(n)]


def get_square_nums_comprehension(n: int = 100_000_000):
    return (i**2 for i in range(n))


def get_square_nums(n: int = 100_000_000):
    for i in range(n):
        yield i**2


def main():
    # print(f"Memory before list: {str(mem_profile.memory_usage())}MB")
    # start_time = time.time_ns()
    # squares_list = get_square_nums_list()
    # end = time.time_ns()
    # print(f"List Squares Time: {end-start_time}")
    # print(f"Memory after list: {str(mem_profile.memory_usage())}MB")

    print(f"Memory before generator: {str(mem_profile.memory_usage())}MB")
    start_time = time.time_ns()
    squares_generator = get_square_nums_comprehension()
    end = time.time_ns()
    print(f"Generator Squares Time: {end - start_time}")
    print(f"Memory after generator: {str(mem_profile.memory_usage())}MB")


if __name__ == "__main__":
    main()
