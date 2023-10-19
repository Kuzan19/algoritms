# Приложения:
# 1. Выделение компоненты
# 2. Подсчет компонент
# 3. Поиск простого цикла
# 4. Проверка двудольности

# С орграфами:
# 5. Выделение сильных компонент Алг. Косарайю
# 6. Топологическая сортировка


def dfs(used: set, graph: dict, vertex):
    """Функция выделения компонетны DFS O(n)"""
    if vertex not in used:
        print(vertex)
        used.add(vertex)
        for neighbour in graph[vertex]:
            dfs(used, graph, neighbour)


def kosarayu():
    """Алгоритм Косарайю (выделение компонент сильной связности)"""
    pass


def taryan(start, graph: dict, visited: list, ans: list):
    """Алгоритм топологической сортировки Тарьяна O(n)"""
    visited[start] = True
    for u in graph[start]:
        if not visited[u]:
            dfs(u, graph, visited)
    ans.append(start)


if __name__ == "__main__":
    graphs = {'5': ['3', '7'],
              '3': ['2', '4'],
              '7': ['8'],
              '2': [],
              '4': ['8'],
              '8': []}

    useds = set()
    visited = []
    ans = []
    print(taryan('5', graphs, visited, ans))
