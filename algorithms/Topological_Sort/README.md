# Topological Sort

## Overview

### Q1: What is Topological Sort?

Ans: Topological Sort is a graph algorithm that produces a linear ordering of the vertices in a Directed Acyclic Graph (DAG). In this ordering, every vertex appears before all vertices that depend on it.

Unlike BFS or DFS, Topological Sort is not used to find paths. Instead, it determines a valid order for completing tasks that have dependencies.

---

### Explaining with an example

Suppose I am preparing for an exam.

Before studying **Dijkstra's Algorithm**, I must first understand:

- Graphs
- BFS
- DFS
- Heaps and Priority Queues

It would not make sense to study Dijkstra before learning these prerequisite topics.

Topological Sort behaves in the same way. It finds an order that satisfies all prerequisite relationships.

Example:

Graphs → BFS → DFS → Dijkstra

One valid ordering is:

Graphs → BFS → DFS → Dijkstra

---

## Requirements

Topological Sort only works on:

- Directed Graphs
- Acyclic Graphs (DAGs)

If a graph contains a cycle, no valid topological ordering exists.

---

## Data Structures Used

- Graph (Adjacency List)
- Visited Set
- Stack (or recursion stack)

---

## Explaining the Algorithm

1. Start DFS from an unvisited node.
2. Continue exploring until no unvisited neighbors remain.
3. Add the finished node to a stack.
4. Repeat for every vertex.
5. Reverse the stack to obtain the topological ordering.

---

## Code Implementations

```python
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
```

Output:

```text
['Graphs', 'DFS', 'Dijkstra', 'BFS']
```

---

## Code Walkthrough

1. `def dfs(graph, node, visited, stack):`

- Defines the recursive DFS helper used to process nodes.

---

2. `if node in visited:`

- Prevents revisiting nodes.

---

3. `visited.add(node)`

- Marks the node as explored before processing neighbors.

---

4. `for neighbor in graph[node]:`

- Explores every outgoing dependency edge from the current node.

---

5. `dfs(graph, neighbor, visited, stack)`

- Recursively finishes all dependencies first.

---

6. `stack.append(node)`

- Adds the node only after all its neighbors are finished.

---

7. `for node in graph:`

- Handles disconnected DAG components by launching DFS from every unvisited node.

---

8. `stack.reverse()`

- Converts finish order into valid topological order.

---

9. `print(stack)`

- Displays one valid topological ordering.

---

## Time Complexity

Here,

V = Number of vertices

E = Number of edges

Time = **O(V + E)**

Each vertex is visited once and every edge is explored once.

Space = **O(V)**

The visited set and recursion stack both require additional memory.

---

## Why does Topological Sort only work on DAGs?

Ans:

A cycle creates a circular dependency.

For example:

A depends on B

B depends on C

C depends on A

There is no valid order in which these tasks can be completed.

---

## Applications

- Course scheduling
- Task scheduling
- Build systems
- Software dependency management
- Project planning
- Package installation

---

## Limitations

- Only works on Directed Acyclic Graphs (DAGs).
- Cannot produce an ordering if the graph contains a cycle.
- Multiple valid topological orders may exist.
