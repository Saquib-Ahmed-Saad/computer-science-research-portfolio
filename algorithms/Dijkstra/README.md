# Dijkstra's Algorithm

## Overview

### Q1: What is Dijkstra's Algorithm?

Ans: Dijkstra's Algorithm is a graph search algorithm used to find the shortest path from a starting node to every other reachable node in a weighted graph with non-negative edge weights.

Unlike BFS, which assumes every edge has the same cost, Dijkstra chooses the path with the lowest total cost.

---

### Explaining with an example

Suppose I am travelling across a kingdom.

Every road has a different travel cost.

Some roads are longer than others, while some may require paying a toll.

Instead of looking for the route with the fewest roads, I want to find the route with the smallest total travel cost.

Dijkstra behaves in the same way.

It continually chooses the unexplored location that currently has the lowest total cost from the starting point.

---

## Requirements

Dijkstra works on:

- Weighted graphs
- Directed or undirected graphs
- Graphs with **non-negative** edge weights

It does **not** guarantee correct results if negative edge weights exist.

---

## Data Structures Used

- Graph (Adjacency List)
- Priority Queue (Min-Heap)
- Distance Dictionary
- Visited Set

---

## Explaining the Algorithm

1. Set every node's distance to infinity.
2. Set the starting node's distance to zero.
3. Insert the starting node into the priority queue.
4. Remove the node with the smallest distance.
5. Update the distances of its neighbors if a shorter path is found.
6. Continue until the priority queue becomes empty.

---

## Code Implementations

```python
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
```

Output:

```text
{
'A': 0,
'B': 3,
'C': 2,
'D': 6
}
```

---

## Code Walkthrough

Follow the same pattern as your BFS and DFS notes.

1. `import heapq`

- Imports Python's priority queue implementation.

---

2. `distances = {}`

- Stores the shortest known distance to every node.

---

3. `float("inf")`

- Represents infinity.
- Initially, every node is assumed unreachable.

---

4. `distances[start] = 0`

- The distance from the start node to itself is zero.

---

5. `priority_queue = [(0, start)]`

- Stores nodes ordered by their current shortest distance.

---

6. `heapq.heappop()`

- Removes the node with the smallest distance.

---

7. `distance = current_distance + weight`

- Calculates the cost of travelling through the current node.

---

8. `if distance < distances[neighbor]`

- Checks whether a better path has been found.

---

9. `heapq.heappush()`

- Inserts the updated distance into the priority queue.

---

## Time Complexity

Here,

V = Number of vertices

E = Number of edges

Time = **O((V + E) log V)**

Space = **O(V)**

The logarithmic factor comes from inserting and removing nodes from the priority queue.

---

## Why does Dijkstra always choose the smallest distance?

Ans:

The algorithm assumes that once a node has the smallest known distance among all unexplored nodes, no future path can produce a smaller distance.

This assumption is valid only when every edge weight is non-negative.

---

## Why doesn't Dijkstra work with negative edges?

Ans:

A negative edge may create a shorter path after a node has already been finalized.

This violates Dijkstra's main assumption and can produce incorrect shortest paths.

---

## Applications

- GPS navigation
- Route planning
- Internet routing
- Network optimization
- Robotics
- Game AI
- Logistics

---

## Limitations

- Does not work correctly with negative edge weights.
- Computes shortest paths from only one source node.
- Can be slower than BFS on unweighted graphs.
