# Breadth-First Search (BFS)

## Overview

### Q1: What is BFS?

Ans: Breadth-First Search is a graph traversal algorithm that explores nodes level by level, visiting all neighboring nodes before moving deeper into the graph. It guarantees the shortest path in terms of the number of edges when all edges have equal cost (an unweighted graph).

### Explaining with an example

Suppose I need to explore a kingdom and find the nearest cities. I begin at the capital and visit every city directly connected to it. After all neighboring cities have been discovered, I then continue exploring from the first city that was discovered, followed by the second, and so on. This creates an outward, level-by-level exploration of the kingdom.

BFS behaves the same way:
- Visit the starting node.
- Visit all of its neighbors.
- Visit the neighbors of those neighbors.
- Continue until every reachable node has been explored.


---


## Data Structures Used

- Queue (FIFO): Stores nodes waiting to be explored.
- Visited Set: A set to keep track of visited nodes
- Adjacency List: Represents the graph efficiently.

---


## Explaining the Algorithm

1. Add the starting node to the queue.
2. Mark it as visited.
3. While the queue is not empty:
   - Remove the front node.
   - Visit it.
   - Add every unvisited neighbor to the queue.
   - Mark those neighbors as visited.


---


## Code Implementations

```python
from collections import deque

def bfs(graph, start):
    """
    Performs Breadth-First Search on a graph.

    Parameters:
        graph (dict): Adjacency list representation of the graph.
        start: Starting node.

    Returns:
        list: Order in which nodes were visited.
    """

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
```

## Code Walkthrough

1. from collections import deque

We use deque because removing from the front of a normal Python list (pop(0)) takes O(n) time. A deque performs popleft() in O(1) time, making it ideal for implementing queues.

2. visited = set()

The visited set keeps track of nodes that have already been explored. This prevents revisiting the same node and avoids infinite loops in graphs containing cycles.

3. queue = deque([start])

The queue stores nodes waiting to be explored. Because it follows the First-In, First-Out (FIFO) principle, nodes are explored level by level.

4. visited.add(start)

The starting node is marked immediately after being placed into the queue to ensure it is never added again.

5. while queue:

Continue exploring until there are no more nodes left to visit.

6. for neighbor in graph[current]:

Look at every node directly connected to the current node.

7. if neighbor not in visited:
    visited.add(neighbor)
    queue.append(neighbor)

If a neighbor has not been visited before:

  - Mark it as visited.
  - Add it to the queue.
  - It will be explored later in FIFO order.

## Example

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print(bfs(graph, 'A'))

The output would be: ['A', 'B', 'C', 'D', 'E', 'F']

---


## Time Complexity

Here,

V = Number of vertices
E = Number of edges

Time = O(V+E). This is because each vertex enters the queue at most once, and every edge is examined once while exploring neighbors.

Space = O(V). This is because the queue may contain many vertices and the visited set stores vertices.

---


## Why does BFS find the shortest path?

Ans: Because BFS explores nodes level by level, it visits every node that is one edge away before any node that is two edges away, every node that is two edges away before any node that is three edges away, and so on. Therefore, the first time a node is reached, BFS has found the path with the fewest edges.

---

## Applications

 - GPS (equal-weight roads)
 - Social networks (degrees of separation)
 - Web crawling
 - Network broadcasting
 - Maze solving
 - Finding connected components
 - Finding shortest path in unweighted graphs


---

## Limitations

 - BFS does not work on problems that have weighted edges or weighted graphs.
 - It can use a significant amount of memory on wide graphs.
 - BFS explores every node at the current level before moving deeper, even if the destination has already been discovered on another branch. This can result in unnecessary exploration.

---



