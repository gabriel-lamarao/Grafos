def prim(graph, root):
    assert type(graph) == dict

    nodes = list(graph)
    nodes.remove(root)

    visited = [root]
    path = []
    next = None

    while nodes:
        distance = float('inf')
        pre = ''
        for s in visited:
            for d in graph[s]:
                if d in visited or s == d:
                    continue
                if graph[s][d] < distance:
                    distance = graph[s][d]
                    pre = s
                    next = d
        path.append((pre, next))
        visited.append(next)
        nodes.remove(next)

    return path
def is_passeio(graph):
    if path[0][0] == path[len(path) - 1][1]:
        return 'Passeio Fechado'
    elif path[0][0] != path[len(path) - 1][1]:
        return 'Passeio Aberto'


def is_ciclo(graph):
    if path[0][0] == path[len(path) - 1][1]:
        return 'É um ciclo'
    elif path[0][0] != path[len(path) - 1][1]:
        return 'Não é um ciclo'


def is_trilha(graph):
    if path[0] == path[len(path) - 1]:
        return 'Trilha Fechado'
    elif path[0] != path[len(path) - 1]:
        return 'Trilha Aberto'

def is_caminho(graph):
    if len(path) > 0:
        return "É um caminho!"
    else:
        return "Não é um caminho!"


if __name__ == '__main__':
    graph_dict = {"s1": {"s1": 0, "s2": 6, "s10": 3, "s12": 4, "s5": 3},
                  "s2": {"s1": 1, "s2": 0, "s10": 4, "s12": 3, "s5": 4},
                  "s10": {"s1": 2, "s2": 6, "s10": 0, "s12": 3, "s5": 4},
                  "s12": {"s1": 1, "s2": 5, "s10": 2, "s12": 0, "s5": 2},
                  "s5": {"s1": 3, "s2": 5, "s10": 7, "s12": 4, "s5": 0}}

    path = prim(graph_dict, "s2")
    print(graph_dict.keys())
    print(is_passeio(path))
    print(is_trilha(path))
    print(is_ciclo(path))
    print(is_caminho(path))
    print(path)
