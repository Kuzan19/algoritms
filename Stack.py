class _Stack:

    def __init__(self, ara=[]):
        self.ara = ara

    def push(self, x):
        self.ara.append(x)

    def pop(self):
        return self.ara.pop()

    def clear(self):
        self.ara.clear()

    def is_empty(self):
        return len(self.ara) == 0

    def show(self):
        print(self.ara)


A = _Stack()

if __name__ == "__main__":
    A.clear()
    A.push(1)
    A.push(2)
    A.push(3)
    A.show()


