from collections import deque


def multi_source_bfs(graph, sources):
    """Compute shortest unweighted distance to the nearest source.

    graph: dict[node, list[node]]
    sources: iterable of source nodes

    returns: (distance, parent)
    """
    distance = {node: float("inf") for node in graph}
    parent = {node: None for node in graph}

    queue = deque()

    for source in sources:
        if source not in graph:
            continue
        if distance[source] != 0:
            distance[source] = 0
            queue.append(source)

    while queue:
        current = queue.popleft()

        for neighbor in graph.get(current, []):
            if distance[neighbor] == float("inf"):
                distance[neighbor] = distance[current] + 1
                parent[neighbor] = current
                queue.append(neighbor)

    return distance, parent


def multi_source_bfs_with_owner(graph, sources):
    """Compute distance and nearest-source owner for each node.

    Ties are resolved by first arrival order in the queue.
    """
    distance = {node: float("inf") for node in graph}
    owner = {node: None for node in graph}

    queue = deque()

    for source in sources:
        if source not in graph:
            continue
        if distance[source] != 0:
            distance[source] = 0
            owner[source] = source
            queue.append(source)

    while queue:
        current = queue.popleft()

        for neighbor in graph.get(current, []):
            if distance[neighbor] == float("inf"):
                distance[neighbor] = distance[current] + 1
                owner[neighbor] = owner[current]
                queue.append(neighbor)

    return distance, owner


if __name__ == "__main__":
    graph_example = {
        "A": ["B"],
        "B": ["A", "C"],
        "C": ["B", "D"],
        "D": ["C", "E"],
        "E": ["D", "F"],
        "F": ["E", "G"],
        "G": ["F"],
    }

    sources_example = ["A", "G"]

    dist, parent = multi_source_bfs(graph_example, sources_example)
    print("distance:", dist)
    print("parent:", parent)

    dist2, owner2 = multi_source_bfs_with_owner(graph_example, sources_example)
    print("distance with owner:", dist2)
    print("owner:", owner2)
