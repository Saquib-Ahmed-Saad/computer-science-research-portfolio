"""Depth-First Search (DFS) example."""


def dfs(graph, node, visited):
    """Print nodes in DFS order starting from node."""
    if node in visited:
        return

    visited.add(node)
    print(node)

    for neighbor in graph.get(node, []):
        dfs(graph, neighbor, visited)


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }

    visited = set()
    print("DFS traversal:")
    dfs(graph, "A", visited)
