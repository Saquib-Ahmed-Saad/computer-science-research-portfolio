from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal = []

    visited.add(start)

    while queue:
        current = queue.popleft()
        traversal.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal




