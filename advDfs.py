def dfs_cycle(graph, node, visited, parent):

    visited.add(node)

    for neighbour in graph[node]:

        if neighbour not in visited:
            if dfs_cycle(graph, neighbour, visited, node):
                return True

        elif parent != neighbour:
            return True

    return False


def has_cycle(graph):

    visited = set()

    for node in graph:
        if node not in visited:
            if dfs_cycle(graph, node, visited, None):
                return True

    return False


graph = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C']
}

print("Cycle Exists:", has_cycle(graph))