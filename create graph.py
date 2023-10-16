def create_graph():
    m, n = [int(x) for x in input().split()]
    V = []
    index = {}
    A = [[0] * n for i in range(m)]
    for i in range(n):
        try:
            v1, v2 = input().split()
            for v in v1, v2:
                if v not in index:
                    V.append(v)
                    index[v] = len(V) - 1
            v1_i = index[v1]
            v2_i = index[v2]
            A[v1_i][v2_i] = 1
        except ValueError:
            break
    return A

print(create_graph())
