def insert_sort(A: list):
    """Сортировка вставками O(n^2)"""
    n = len(A)
    for top in range(1, n):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1


def choise_sort(A: list):
    """Сортировка выбором O(n^2)"""
    n = len(A)
    for pos in range(0, n - 1):
        for k in range(pos + 1, n):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def bubble_sort(A: list):
    """Сортировка пузырьками O(n^2)"""
    n = len(A)
    for bypass in range(1, n):
        for k in range(0, n - bypass):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]


def count_sort(A: list):
    """Сортировка подсчетом O(n)"""
    n = len(A)
    F = [0] * (n + 1)
    for i in range(1, n + 1):
        F[A[i]] += F[A[i]] + 1

    F[0] = F[0] - 1
    for i in range(1, n + 1):
        F[i] = F[i] + F[i - 1]

    result = [None] * len(A)

    for x in reversed(A):
        result[F[x]] = x
        F[x] = F[x] - 1

    return result


def merge(A: list, B: list):
    """Сортировка слиянием отсортированных масивов O(n)"""
    c = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            c[n] = A[i]
            i += 1
            n += 1
        else:
            c[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        c[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        c[n] = B[k]
        k += 1
        n += 1
    return c


def merge_sort(A: list):
    if len(A) <= 1:
        return
    middle = len(A) // 2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]


def huar_sort(A):
    """Сортировка Чарлза Хоара O(n^2 - bad time)"""
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    R = []
    M = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    huar_sort(L)
    huar_sort(R)
    k = 0
    for x in L+M+R:
        A[k] = x
        k += 1
    return


def check_sorted(A, ascending = True):
    flag = True
    coef = 2 * int(ascending) - 1
    for i in range(0, len(A)-1):
        if coef * A[i] > coef * A[i+1]:
            flag = False
            break
    return flag


mist = [-6, 2, 4, -12, 46, 73]

if __name__ == '__main__':
    pass

