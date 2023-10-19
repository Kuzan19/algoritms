def create_graph():
    m, n = [int(x) for x in input().split()]
    G = {}
    for i in range(n):
        try:
            v1, v2 = input().split()
            for v, u in (v1, v2), (v2, v1):
                if v not in G:
                    G[v] = {u}
                else:
                    G[v].add(u)
        except ValueError:
            break
    return G


if __name__ == "__main__":
    print(create_graph())
