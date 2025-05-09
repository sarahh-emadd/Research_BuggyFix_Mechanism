def breadth_first_search(graph, start):
    # Replace this with your buggy or fixed implementation
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend([n for n in graph.get(node, []) if n not in visited])
    return visited


def test_breadth_first_search():
    test_cases = [
        (
            {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": [], "F": []},
            "A",
            ["A", "B", "C", "D", "E", "F"],
        ),
        (
            {"1": ["2", "3"], "2": ["4"], "3": [], "4": []},
            "1",
            ["1", "2", "3", "4"],
        ),
        (
            {"x": ["y"], "y": ["z"], "z": []},
            "x",
            ["x", "y", "z"],
        ),
        (
            {"a": ["b"], "b": ["a"]},
            "a",
            ["a", "b"],
        ),
        (
            {},
            "a",
            ["a"],
        ),
    ]

    for i, (graph, start, expected) in enumerate(test_cases):
        try:
            result = breadth_first_search(graph, start)
            assert result == expected, f"Test {i+1} failed: got {result}, expected {expected}"
            print(f"Test {i+1} passed ✅")
        except Exception as e:
            print(f"Test {i+1} raised an exception ❌: {e}")

if __name__ == "__main__":
    test_breadth_first_search()