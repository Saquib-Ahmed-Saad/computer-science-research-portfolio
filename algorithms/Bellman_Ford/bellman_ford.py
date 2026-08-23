def bellman_ford(vertices, edges, start):
    """Compute single-source shortest paths with possible negative weights.

    Args:
        vertices: iterable of vertices
        edges: iterable of (u, v, weight)
        start: source vertex

    Returns:
        (distance, parent, has_negative_cycle)
        If a reachable negative cycle exists, returns (None, None, True).
    """
    distance = {vertex: float("inf") for vertex in vertices}
    parent = {vertex: None for vertex in vertices}

    if start not in distance:
        return None, None, False

    distance[start] = 0

    # Relax all edges up to V - 1 times.
    for _ in range(len(distance) - 1):
        updated = False

        for u, v, weight in edges:
            if distance.get(u, float("inf")) == float("inf"):
                continue

            new_distance = distance[u] + weight
            if new_distance < distance.get(v, float("inf")):
                distance[v] = new_distance
                parent[v] = u
                updated = True

        # Early exit if no improvement in a full round.
        if not updated:
            break

    # One extra pass to detect reachable negative cycles.
    for u, v, weight in edges:
        if distance.get(u, float("inf")) == float("inf"):
            continue

        if distance[u] + weight < distance.get(v, float("inf")):
            return None, None, True

    return distance, parent, False


def reconstruct_path(parent, start, target):
    """Reconstruct shortest path from start to target using parent pointers."""
    if parent is None:
        return None

    path = []
    current = target

    while current is not None:
        path.append(current)

        if current == start:
            break

        current = parent.get(current)

    if not path or path[-1] != start:
        return None

    path.reverse()
    return path


if __name__ == "__main__":
    vertices_example = ["A", "B", "C", "D"]
    edges_example = [
        ("A", "B", 4),
        ("A", "C", 5),
        ("B", "C", -2),
        ("C", "D", 3),
    ]

    distance_map, parent_map, has_cycle = bellman_ford(
        vertices_example,
        edges_example,
        "A",
    )

    print("distance:", distance_map)
    print("parent:", parent_map)
    print("reachable_negative_cycle:", has_cycle)

    if not has_cycle and distance_map is not None:
        print("path A -> D:", reconstruct_path(parent_map, "A", "D"))
