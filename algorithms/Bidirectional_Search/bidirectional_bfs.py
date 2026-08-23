from collections import deque


def expand_level(graph, queue, own_visited, other_visited, parent):
    """Expand exactly one BFS level from one side.

    Returns the meeting node if found, otherwise None.
    """
    level_size = len(queue)

    for _ in range(level_size):
        current = queue.popleft()

        for neighbor in graph.get(current, []):
            if neighbor in own_visited:
                continue

            own_visited.add(neighbor)
            parent[neighbor] = current
            queue.append(neighbor)

            if neighbor in other_visited:
                return neighbor

    return None


def build_path(meeting, forward_parent, backward_parent):
    """Reconstruct full path from source to target via the meeting node."""
    path = []

    current = meeting
    while current is not None:
        path.append(current)
        current = forward_parent[current]
    path.reverse()

    current = backward_parent[meeting]
    while current is not None:
        path.append(current)
        current = backward_parent[current]

    return path


def bidirectional_bfs(graph, start, target):
    """Find shortest path in an unweighted graph using bidirectional BFS.

    graph: dict[node, list[node]]
    returns: list[node] path from start to target, or None if unreachable
    """
    if start == target:
        return [start]

    if start not in graph or target not in graph:
        return None

    forward_queue = deque([start])
    backward_queue = deque([target])

    forward_visited = {start}
    backward_visited = {target}

    forward_parent = {start: None}
    backward_parent = {target: None}

    while forward_queue and backward_queue:
        meeting = expand_level(
            graph,
            forward_queue,
            forward_visited,
            backward_visited,
            forward_parent,
        )
        if meeting is not None:
            return build_path(meeting, forward_parent, backward_parent)

        meeting = expand_level(
            graph,
            backward_queue,
            backward_visited,
            forward_visited,
            backward_parent,
        )
        if meeting is not None:
            return build_path(meeting, forward_parent, backward_parent)

    return None


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

    print(bidirectional_bfs(graph_example, "A", "G"))
