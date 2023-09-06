from Sort import insert_sort


def left_bound(A: list, key: int):
    """Находим левую границу повторяющихся значений массива O(Log2N)"""
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(A: list, key: int):
    """Находим левую границу повторяющихся значений массива O(Log2N)"""
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right


mist = [1, 4, 6, -2, -2, -2, 5, 6, 23, 73, 7, 14, 85]

if __name__ == "__main__":
    print(mist)
    insert_sort(mist)
    print(left_bound(mist, 4))
    print(right_bound(mist, 4))
