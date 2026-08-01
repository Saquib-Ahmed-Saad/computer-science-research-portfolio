# Depth-First Search (DFS)

## Overview

Q1: What is DFS?

Ans: Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible along a path before backtracking. Unlike Breadth-First Search, which explores level by level, DFS follows one branch until there are no more unvisited nodes before returning to explore other branches.

Explaining with an example:

Suppose I am exploring a kingdom filled with castles connected by roads. Instead of visiting every nearby castle first, I choose one road and continue travelling until I cannot go any further. Only then do I return to the previous castle and explore the next unexplored road. I continue this process until every reachable castle has been visited.

DFS behaves the same way:
- Visit the starting node.
- Continue exploring one unvisited neighbor.
- Repeat until reaching a dead end.
- Backtrack to the previous node.
- Continue exploring remaining unexplored paths.

---

## Data Structures Used

- Stack (explicit stack or the program's call stack through recursion)
- A set to keep track of visited nodes
- Graph (Adjacency List)

---

## Explaining the Algorithm

1. Start at the source node.
2. Mark it as visited.
3. Visit one unvisited neighbor.
4. Repeat until no unvisited neighbors remain.
5. Backtrack to the previous node.
6. Continue until every reachable node has been explored.

---

## Python Implementation

```python
def dfs(graph, node, visited):
    """
    Performs Depth-First Search on a graph.

    Parameters:
        graph (dict): Adjacency list representation of the graph.
        node: Starting node.
        visited (set): Stores visited nodes.

    Returns:
        None
    """

    # If the node has already been visited,
    # there is nothing left to explore.
    if node in visited:
        return

    # Mark the current node as visited.
    visited.add(node)

    # Visit the current node.
    print(node)

    # Explore each neighboring node.
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)
```

## Code Walkthrough

### 1. `def dfs(graph, node, visited):`

This function performs a Depth-First Search starting from a given node.

- `graph` is the adjacency list representation of the graph.
- `node` is the current node being explored.
- `visited` is a set that keeps track of nodes that have already been visited.

---

### 2. `if node in visited:`

Before exploring a node, we first check whether it has already been visited.

If it has, we simply return because there is nothing left to explore.

This prevents revisiting nodes and avoids infinite loops in graphs containing cycles.

---

### 3. `visited.add(node)`

Once we know the node has not been visited, we add it to the visited set.

This ensures we never process the same node twice.

---

### 4. `print(node)`

This represents visiting the node.

For this implementation, we simply print the node as soon as we reach it.

---

### 5. `for neighbor in graph[node]:`

Look at every node directly connected to the current node.

DFS explores one neighbor completely before moving on to the next.

---

### 6. `dfs(graph, neighbor, visited)`

This is the recursive call.

Instead of placing the neighbor into a queue like BFS, DFS immediately begins exploring that neighbor.

Once that path reaches a dead end, the function automatically returns to the previous node (backtracking) and continues exploring the remaining neighbors.

## Example

```python
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

visited = set()

dfs(graph, "A", visited)
```

The output would be:

```text
A
B
D
E
C
F
```

---


## Time Complexity

Here,

V = Number of vertices

E = Number of edges

Time = O(V + E)

Each vertex is visited once, and every edge is explored once.

Space = O(V)

The visited set stores vertices, and the recursion stack may contain up to V nodes in the worst case.

---

## Why doesn't DFS guarantee the shortest path?

Ans: DFS always continues down one branch before considering any alternatives. Because it commits to the first available path, it may reach a destination through a much longer route before discovering a shorter one elsewhere in the graph.

---

## Applications

- Maze solving
- Topological sorting
- Cycle detection
- Connected components
- Dependency resolution
- Path existence checking

---

## Limitations

- Does not guarantee the shortest path.
- Recursive implementations may cause stack overflow on very deep graphs.
- Can waste time exploring long unnecessary branches before finding the destination.