from Heap import Heap

li = [46, 15, 3, 4, 21, 79, 61]


def heap_sort(ar: list):
    """Сортировка кучей с помощью класса Heap"""
    heap = Heap()
    for item in ar:
        heap.insert(item)
    return heap


if __name__ == "__main__":
    print(heap_sort(li))

