def dfs(graph, node, visited, stack):
    if node in visited:
        return

    visited.add(node)

    for neighbor in graph[node]:
        dfs(graph, neighbor, visited, stack)

    stack.append(node)


graph = {
    "Graphs": ["BFS", "DFS"],
    "BFS": [],
    "DFS": ["Dijkstra"],
    "Dijkstra": [],
}

visited = set()
stack = []

for node in graph:
    dfs(graph, node, visited, stack)

stack.reverse()

print("Topological Order:")
print(stack)
