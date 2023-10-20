# Приложения:
# 1. Выделение компоненты
# 2. Подсчет компонент
# 3. Поиск простого цикла
# 4. Проверка двудольности

# С орграфами:
# 5. Выделение сильных компонент Алг. Косарайю
# 6. Топологическая сортировка


def dfs(vertex, graph: dict, used: set, stack: list):
    """Функция выделения компонетны DFS"""
    print(vertex, end=' ')
    used.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in used:
            dfs(neighbor, graph, used, stack)
    stack.append(vertex)


def dfs_r(vertex, graph, used):
    """Обратый проход по графу DFS_R"""
    print(vertex, end=' ')
    used.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in used:
            dfs_r(neighbor, graph, used)


def invert(graph: dict):
    """Процедура инвертирования графа"""
    H = dict()
    for vertex in graph:
        H[vertex] = set()
    for vertex in graph:
        for v in graph[vertex]:
            H[v].add(vertex)
    return H


def printg(graph: dict):
    """Форматированный вывод графа"""
    for vertex in graph:
        print(f'{vertex}: {graph[vertex]}')


def n_strongly_comp(graph):
    """Процедура подсчета компонент сильной связности орграфа"""
    used = set()
    stack = []
    N = 0
    # делаем прямой обход орграфа и заполняем попутно стек
    # считаем компоненты "слабой" связности
    for vertex in graph:
        if vertex not in used:
            print(f'graph weekly connected component #{N}: ', end='')
            dfs(vertex, graph, used, stack)
            print('')
            N += 1
    print(f'N weekly comps = {N}')
    print(f'stack: {stack}')
    # получаем инвертированный орграф
    H = invert(graph)
    print(f'inverted graph:')
    printg(H)
    # обходим инвертированный орграф,
    # учитывая порядок вершин в стеке
    # считаем компоненты сильной связности
    N = 0
    used = set()
    print('')
    while stack != []:
        vertex = stack.pop()
        if vertex not in used:
            print(f'strongly comp #{N}: ', end='')
            dfs_r(vertex, H, used)
            print('')
            N += 1
    return N


if __name__ == "__main__":
    graphs = {'5': ['3', '7'],
              '3': ['2', '4'],
              '7': ['8'],
              '2': [],
              '4': ['8'],
              '8': []}
    print(n_strongly_comp(graphs))
