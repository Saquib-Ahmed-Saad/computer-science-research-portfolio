import heapq

def dijkstra(graph, start):
    distances = {}

    for node in graph:
        distances[node] = float("inf")

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        for neighbor, weight in graph[current_node]:

            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("D", 3)],
    "C": [("B", 1), ("D", 5)],
    "D": []
}

print(dijkstra(graph, "A"))
