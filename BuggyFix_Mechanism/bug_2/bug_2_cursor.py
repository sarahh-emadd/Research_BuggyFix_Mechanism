#bug_2fix
def breadth_first_search(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            # Only add unvisited neighbors to avoid cycles
            queue.extend(v for v in graph[vertex] if v not in visited)
    return visited
