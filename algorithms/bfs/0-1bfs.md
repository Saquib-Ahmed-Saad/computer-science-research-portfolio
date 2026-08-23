# 0-1 BFS

## Overview

### Q1: What is 0-1 BFS?

Ans: 0-1 BFS is a shortest-path algorithm for graphs where every edge weight is either 0 or 1. It sits between BFS and Dijkstra. Like BFS, it is very efficient and simple. Like Dijkstra, it uses distances and relaxation to find minimum total cost, not just minimum number of edges.

### Q2: Why is it called 0-1 BFS?

Ans: It is called 0-1 BFS because it only works under one strict condition: every edge must have weight 0 or 1. That binary weight structure is what makes the deque trick possible.

---

## Intuition

### Q3: Why can normal BFS fail on weighted edges?

Ans: BFS explores level by level, which is perfect when every edge has the same cost. But if one edge costs 1 and another costs 0, then fewer edges does not always mean cheaper total path. So BFS can return a path with fewer hops but higher cost.

Example:

- A -> B has cost 1
- A -> C has cost 0
- C -> B has cost 0

Direct path A -> B costs 1, but path A -> C -> B costs 0. That is why plain BFS is not enough here.

### Q4: Why not just use Dijkstra?

Ans: We can use Dijkstra, and it will be correct. But Dijkstra uses a priority queue, so it usually runs in O((V + E) log V). For 0/1 weights, 0-1 BFS gives the same correctness with a deque and linear time O(V + E).

---

## Data Structures Used

- Deque: stores nodes to process, with insertions at both front and back.
- Distance map: keeps the best known distance from source to each node.
- Optional parent map: helps reconstruct the actual shortest path.
- Adjacency list: graph representation.

---

## Core Rule

### Q5: What is the most important rule in 0-1 BFS?

Ans: The rule is simple:

- If edge weight is 0, push neighbor to the front.
- If edge weight is 1, push neighbor to the back.

In short:

- 0 edge -> appendleft()
- 1 edge -> append()

This keeps cheaper states in front without needing a heap.

---

## Algorithm Steps

1. Initialize all distances as infinity.
2. Set distance[start] = 0.
3. Put start in deque.
4. While deque is not empty:
   - Pop from front.
   - For each neighbor, compute new_distance = dist[current] + weight.
   - If new_distance is better, update distance.
   - If weight is 0, push neighbor to front.
   - If weight is 1, push neighbor to back.

---

## Python Implementation

```python
from collections import deque

def zero_one_bfs(graph, start):
    distance = {node: float("inf") for node in graph}
    parent = {node: None for node in graph}

    distance[start] = 0
    dq = deque([start])

    while dq:
        current = dq.popleft()

        for neighbor, weight in graph[current]:
            new_distance = distance[current] + weight

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                parent[neighbor] = current

                if weight == 0:
                    dq.appendleft(neighbor)
                else:
                    dq.append(neighbor)

    return distance, parent
```

---

## Code Walkthrough

1. distance map

Stores the best cost found so far for every node.

2. parent map

Stores from where we reached each node with best cost.

3. deque

Acts like a two-priority queue: current cost states at front, cost+1 states at back.

4. relaxation condition

If dist[current] + weight < dist[neighbor], we found a better route and must update.

5. appendleft vs append

Weight 0 means same total cost, so process early. Weight 1 means one extra cost, so process later.

---

## Example

```python
graph = {
    "A": [("B", 1), ("C", 0)],
    "B": [("D", 0)],
    "C": [("D", 1)],
    "D": []
}

distance, parent = zero_one_bfs(graph, "A")
print(distance)
print(parent)
```

Expected distance output:

- A: 0
- B: 1
- C: 0
- D: 1

---

## Why Distance Instead of Visited

### Q6: Why can we not rely only on visited in 0-1 BFS?

Ans: In normal BFS, first visit is final for shortest path in edge-count terms. In 0-1 BFS, first discovery might not be cheapest in cost terms. A node can be discovered again with a lower total cost, so distance comparison is the real decision rule.

Key question is not:

Have I seen this node before?

Key question is:

Did I find a cheaper path to this node?

---

## Complexity

### Q7: What is the time and space complexity?

Ans:

- Time: O(V + E)
- Space: O(V + E) including graph storage
- Auxiliary space: O(V) for distance, parent, and deque

This is the main performance reason people choose 0-1 BFS for binary-weight graphs.

---

## Comparison

- BFS
  - Use when graph is unweighted or all edges equal
  - Typical complexity: O(V + E)

- 0-1 BFS
  - Use when weights are only 0 or 1
  - Typical complexity: O(V + E)

- Dijkstra
  - Use when weights are non-negative and not limited to 0/1
  - Typical complexity: O((V + E) log V)

- Bellman-Ford
  - Use when negative weights exist
  - Typical complexity: O(VE)

---

## Directed vs Undirected Graphs

### Q8: Does 0-1 BFS work for both directed and undirected graphs?

Ans: Yes. The algorithm does not change. For undirected edges, just store both directions in adjacency list.

---

## Edge Cases

### Q9: Can 0-1 BFS handle disconnected graphs?

Ans: Yes. Unreachable nodes remain at infinity from the chosen source.

### Q10: Can 0-1 BFS handle negative weights?

Ans: No. It requires every weight to be exactly 0 or 1.

### Q11: Can it handle weight 2?

Ans: Not in standard form. For general non-negative weights, use Dijkstra.

---

## Path Reconstruction

### Q12: How do I get the actual shortest path, not just distance?

Ans: Use the parent map. Start from target, keep following parent[target], and reverse the collected list at the end.

---

## Practical Use Cases

- Minimum walls broken in grid problems
- Preferred vs non-preferred route cost models
- Binary penalty routing
- Fast shortest path in large sparse binary-weight graphs

---

## Final Mental Model

Thinking of it like this:

- BFS says: everyone waits in one line.
- Dijkstra says: always pick globally cheapest next state.
- 0-1 BFS says: if move is free, go to front; if move costs one, go to back.

That one rule is the heart of the algorithm.
