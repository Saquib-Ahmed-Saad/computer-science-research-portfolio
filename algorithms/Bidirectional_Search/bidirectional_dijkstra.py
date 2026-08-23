import heapq


def reverse_graph(graph):
    """Build reverse adjacency list for directed graphs.

    graph format: dict[node, list[tuple[neighbor, weight]]]
    """
    rev = {node: [] for node in graph}

    for u, edges in graph.items():
        for v, w in edges:
            if v not in rev:
                rev[v] = []
            rev[v].append((u, w))

    return rev


def reconstruct_path(meeting, parent_f, parent_b):
    """Reconstruct source -> meeting -> target using two parent maps."""
    path = []

    current = meeting
    while current is not None:
        path.append(current)
        current = parent_f.get(current)
    path.reverse()

    current = parent_b.get(meeting)
    while current is not None:
        path.append(current)
        current = parent_b.get(current)

    return path


def _settle_one_direction(
    pq,
    dist,
    settled,
    other_dist,
    other_settled,
    parent,
    graph,
    best_cost,
    best_meeting,
):
    """Pop and relax one settled node for one side of bidirectional Dijkstra."""
    while pq:
        d_u, u = heapq.heappop(pq)
        if u in settled:
            continue
        if d_u != dist[u]:
            continue

        settled.add(u)

        if u in other_settled:
            candidate = dist[u] + other_dist[u]
            if candidate < best_cost:
                best_cost = candidate
                best_meeting = u

        for v, w in graph.get(u, []):
            nd = d_u + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))

                if v in other_settled:
                    candidate = dist[v] + other_dist[v]
                    if candidate < best_cost:
                        best_cost = candidate
                        best_meeting = v

        return best_cost, best_meeting

    return best_cost, best_meeting


def bidirectional_dijkstra(graph, start, target):
    """Shortest path for non-negative weighted directed/undirected graphs.

    graph format: dict[node, list[tuple[neighbor, weight]]]
    returns: (distance, path) or (float('inf'), None) if unreachable
    """
    if start == target:
        return 0, [start]

    if start not in graph or target not in graph:
        return float("inf"), None

    rev = reverse_graph(graph)

    dist_f = {start: 0}
    dist_b = {target: 0}

    parent_f = {start: None}
    parent_b = {target: None}

    settled_f = set()
    settled_b = set()

    pq_f = [(0, start)]
    pq_b = [(0, target)]

    best_cost = float("inf")
    best_meeting = None

    while pq_f and pq_b:
        top_f = pq_f[0][0]
        top_b = pq_b[0][0]

        if top_f + top_b >= best_cost:
            break

        if top_f <= top_b:
            best_cost, best_meeting = _settle_one_direction(
                pq_f,
                dist_f,
                settled_f,
                dist_b,
                settled_b,
                parent_f,
                graph,
                best_cost,
                best_meeting,
            )
        else:
            best_cost, best_meeting = _settle_one_direction(
                pq_b,
                dist_b,
                settled_b,
                dist_f,
                settled_f,
                parent_b,
                rev,
                best_cost,
                best_meeting,
            )

    if best_meeting is None:
        return float("inf"), None

    return best_cost, reconstruct_path(best_meeting, parent_f, parent_b)


if __name__ == "__main__":
    graph_example = {
        "A": [("B", 4), ("C", 1)],
        "B": [("D", 1)],
        "C": [("B", 2), ("D", 5)],
        "D": [("E", 3)],
        "E": [],
    }

    dist, path = bidirectional_dijkstra(graph_example, "A", "E")
    print("Distance:", dist)
    print("Path:", path)
