import heapq

def heuristic(node, goal):
    estimates = {
        "A": 7,
        "B": 6,
        "C": 2,
        "D": 1,
        "E": 0
    }

    return estimates[node]

def a_star(graph, start, goal):

    g_score = {}

    for node in graph:
        g_score[node] = float("inf")

    g_score[start] = 0

    priority_queue = [(heuristic(start, goal), start)]

    while priority_queue:

        current_f, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            return g_score[current_node]

        for neighbor, weight in graph[current_node]:

            tentative_g = g_score[current_node] + weight

            if tentative_g < g_score[neighbor]:

                g_score[neighbor] = tentative_g

                f_score = tentative_g + heuristic(neighbor, goal)

                heapq.heappush(priority_queue, (f_score, neighbor))

graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2)],
    "C": [("D", 1)],
    "D": [("E", 3)],
    "E": []
}

print(a_star(graph, "A", "E"))
