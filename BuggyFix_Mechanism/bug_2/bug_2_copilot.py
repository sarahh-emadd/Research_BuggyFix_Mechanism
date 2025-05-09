 # fix Bug2 github
def breadth_first_search(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph.get(vertex, []))
    return visited 