# Graph Theory

## Overview

### Q1: What is Graph Theory?

Ans: Graph Theory is a branch of mathematics and computer science that studies graphs. A graph is a collection of vertices (nodes) connected by edges. Graphs are used to model relationships between objects and are fundamental to many algorithms in computer science.

Graphs appear in many real-world applications such as:

- GPS navigation
- Social networks
- Computer networks
- Robotics
- Artificial Intelligence
- Recommendation systems
- Project scheduling

Almost every graph algorithm begins with understanding graph theory.

---

## What is a Graph?

A graph consists of:

- **Vertices (Nodes):** The objects being represented.
- **Edges:** The connections between vertices.

Example:

```
A ----- B
|       |
|       |
C ----- D
```

Here,

Vertices:

- A
- B
- C
- D

Edges:

- A-B
- A-C
- B-D
- C-D

---

## Important Terminology

### Vertex (Node)

A single object inside a graph.

Example:

```
A ----- B
```

A and B are vertices.

---

### Edge

A connection between two vertices.

Example:

```
A ----- B
```

The line represents an edge.

---

### Path

A sequence of connected vertices.

Example:

```
A -> B -> C -> D
```

---

### Degree

The number of edges connected to a vertex.

Example:

```
A
|
B---C
```

Vertex B has degree 3.

---

## Weighted vs Unweighted Graphs

### Unweighted Graph

Every edge has the same cost.

Example:

```
A ---- B ---- C
```

BFS works on unweighted graphs.

---

### Weighted Graph

Each edge has a numerical cost.

```
A --4--> B
 \2
  \
   C
```

Dijkstra's Algorithm and A* use weighted graphs.

---

## Graph Representations

### Adjacency List

Stores every node along with its neighbors.

Example:

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}
```

Advantages:

- Memory efficient
- Best for sparse graphs
- Used throughout this repository

---

### Adjacency Matrix

Represents the graph using a table.

```
    A B C D
A [ 0 1 1 0 ]
B [ 1 0 0 1 ]
C [ 1 0 0 0 ]
D [ 0 1 0 0 ]
```

Advantages:

- Constant-time edge lookup
- Better suited for dense graphs

---

# Trees

A tree is a graph that:

- is connected
- contains no cycles

Example:

```
      A
     / \
    B   C
   / \
  D   E
```

This is a tree because:

- Every node is reachable.
- There are no loops.

### Important Tree Terms

#### Root

The starting node.

```
A
```

A is the root.

---

#### Parent

If an edge connects A to B,

```
A
|
B
```

A is B's parent.

---

#### Child

```
A
|
B
```

B is A's child.

---

#### Leaf

A node with no children.

```
    A
   / \
  B   C
 /
D
```

C and D are leaves.

---

#### Depth

The distance from the root.

Example:

```
A depth = 0
B depth = 1
D depth = 2
```

---

#### Height

The length of the longest path from a node to one of its descendants.

Example:

```
A
|
B
|
D
```

Height of A = 2.

---

### Why Trees Matter

Trees appear everywhere:

- File systems
- Family trees
- Decision trees
- Organization charts
- Binary Search Trees
- BFS and DFS are often first learned using trees.

---

# Connected Components

A connected component is a group of vertices where every vertex can reach every other vertex.

Example:

```
A --- B --- C

D --- E
```

This graph contains two connected components.

Component 1:

A, B, C

Component 2:

D, E

---

### Why Components Matter

Real-world examples:

- Friend groups in social networks
- Computer networks
- Internet clusters

DFS and BFS can be used to identify connected components.

---

# Directed Graphs

A directed graph contains edges with directions.

Example:

```
A -> B
```

does **not** imply

```
B -> A
```

Example:

Instagram.

You may follow someone without them following you back.

---

# Directed Acyclic Graphs (DAGs)

DAG stands for:

**Directed Acyclic Graph**

Directed:

```
A -> B
```

Acyclic:

No loops.

Graph:

Collection of nodes and edges.

Example:

```
Math

|
V

Algorithms

|
V

Artificial Intelligence
```

You cannot study AI before Algorithms.

---

### Why DAGs Matter

Many real systems are DAGs.

Examples:

Course prerequisites

```
Calculus I

|
V

Calculus II

|
V

Differential Equations
```

Software build systems

```
Library

|
V

Program
```

Project planning

```
Design

|
V

Implementation

|
V

Testing
```

---

# Topological Sorting

Topological Sort finds a valid ordering of tasks with dependencies.

Example:

Dependencies:

```
A -> B
A -> C
B -> D
C -> D
```

Valid orderings include:

```
A B C D
```

or

```
A C B D
```

Both satisfy every dependency.

DFS is commonly used to perform Topological Sort.

---

# Sparse vs Dense Graphs

### Sparse Graph

Contains relatively few edges.

Example:

1000 nodes

1500 edges

Advantages:

- Less memory
- Faster traversal

---

### Dense Graph

Contains many edges.

Example:

1000 nodes

450,000 edges

Algorithms often behave differently on dense graphs because many more neighboring vertices must be explored.

---

# Cycles

A cycle occurs when you can start at one vertex and eventually return to it.

Example:

```
A -> B
^    |
|    v
D <- C
```

Starting at A:

```
A -> B -> C -> D -> A
```

This forms a cycle.

---

### Why Cycles Matter

Cycles create dependency problems.

Example:

Task A depends on Task B.

Task B depends on Task A.

Neither task can begin.

Many algorithms require cycle-free graphs.

DFS is commonly used to detect cycles.

---

# Spanning Trees

A spanning tree is a tree that connects every vertex in a graph without forming any cycles.

Example:

Original graph:

```
A ---- B
| \    |
|  \   |
C ---- D
```

A possible spanning tree:

```
A ---- B
|
|
C ---- D
```

Every vertex remains connected, but unnecessary edges have been removed.

---

### Why Spanning Trees Matter

Spanning trees are used in:

- Computer networking
- Routing
- Network optimization
- Minimum Spanning Tree algorithms such as Prim's and Kruskal's

---

# Why Graph Theory Matters

Graph Theory provides the mathematical foundation for many algorithms studied in computer science.

Every algorithm in this repository builds upon these concepts.

Understanding graphs is essential before studying:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Topological Sort
- Dijkstra's Algorithm
- A* Search
- Minimum Spanning Trees
- Network Flow Algorithms
