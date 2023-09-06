def fib(n):
    """Рекурсивная функция поиска числа Фибоначчи O(Fib n)"""
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_dynamic(n):
    """Динамическая функция поиска числа Фибоначчи O(n)"""
    fib = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


if __name__ == "__main__":
    print(fib_dynamic(10))
    