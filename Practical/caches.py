from functools import cache, lru_cache


# @lru_cache(maxsize=10)
# @cache
def fibonacci(n: int):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def main():
    for n in range(200):
        print(n, fibonacci(n))


if __name__ == "__main__":
    main()
