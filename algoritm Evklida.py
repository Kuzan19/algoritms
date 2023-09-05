def gcd(a, b):
    """Рекурсия для решения алгоритма евклида"""
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:  # a < b
        return gcd(a, b - a)


def gcd2(a, b):
    """Второй вариант рекурсии для решения алгоритма евклида"""
    if b == 0:
        return a
    else:  # a < b
        return gcd2(b, a % b)


def gcd3(a, b):
    """Третий вариант рекурсии для решения алгоритма евклида"""
    return a if b == 0 else gcd3(b, a % b)
