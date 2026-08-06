# A* Search Algorithm

## Overview

### Q1: What is A* Search?

Ans: A* (A-Star) is a graph search algorithm used to find the shortest path between two nodes. Like Dijkstra's Algorithm, it works on weighted graphs with non-negative edge weights. However, A* uses a heuristic to estimate the remaining distance to the goal, allowing it to search more efficiently.

Instead of exploring every promising path equally, A* prioritizes paths that appear to move closer to the destination.

---

### Explaining with an example

Suppose I am travelling across a kingdom to reach a castle.

Dijkstra would consider every possible route based only on the distance already travelled.

A* goes one step further.

In addition to the distance already travelled, it estimates how far the castle still is. This allows A* to focus on routes that seem to head toward the destination instead of exploring every possible direction.

---

## Requirements

A* works on:

- Weighted graphs
- Directed or undirected graphs
- Graphs with non-negative edge weights
- Problems where a heuristic can estimate the remaining distance

---

## Data Structures Used

- Graph (Adjacency List)
- Priority Queue (Min-Heap)
- Distance Dictionary (g-score)
- Heuristic Function (h-score)
- Estimated Total Cost (f-score)
- Visited Set (optional depending on implementation)

---

## Explaining the Algorithm

1. Set the starting node's distance (g-score) to zero.
2. Estimate the remaining distance using a heuristic (h-score).
3. Compute:

   **f(n) = g(n) + h(n)**

4. Insert the starting node into the priority queue.
5. Remove the node with the smallest f-score.
6. Update neighboring nodes if a shorter path is found.
7. Continue until the destination is reached.

---

## Code Implementations

```python
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
```

Output:

```text
6
```

---

## Code Walkthrough

1. `import heapq`

- Imports Python's priority queue.

---

2. `heuristic()`

- Returns an estimate of the remaining distance to the goal.

---

3. `g_score`

- Stores the actual shortest distance from the start.

---

4. `priority_queue`

- Stores nodes ordered by their `f-score`.

---

5. `tentative_g`

- Calculates the cost of travelling to a neighboring node.

---

6. `f_score`

```text
f(n) = g(n) + h(n)
```

- Actual distance travelled.
- Estimated remaining distance.

---

7. `heapq.heappush()`

- Inserts the updated node according to its priority.

---

## Time Complexity

Worst Case:

Time = **O((V + E) log V)**

Space = **O(V)**

If the heuristic is poor, A* behaves similarly to Dijkstra's Algorithm.

A good heuristic can significantly reduce the number of explored nodes.

---

## What is a Heuristic?

A heuristic is an estimate of the remaining cost from the current node to the goal.

It guides A* toward promising paths while still allowing the algorithm to find the optimal path when the heuristic is admissible.

---

## Why is A* usually faster than Dijkstra?

Ans:

Dijkstra explores nodes solely based on the distance already travelled.

A* combines:

- Distance already travelled.
- Estimated remaining distance.

This allows A* to ignore many unnecessary paths and reach the goal more quickly.

---

## Applications

- GPS navigation
- Robotics
- Video game pathfinding
- Autonomous vehicles
- Warehouse robots
- Route planning
- AI movement systems

---

## Limitations

- Requires a suitable heuristic.
- A poor heuristic reduces A* to Dijkstra's Algorithm.
- Performance depends heavily on the quality of the heuristic.
