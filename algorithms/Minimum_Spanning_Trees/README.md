# Minimum Spanning Trees (MST)

## Overview
A Minimum Spanning Tree (MST) is a spanning tree of a connected, weighted, undirected graph that connects every vertex while having the smallest possible total edge weight.

An MST must:

- Connect every vertex.
- Contain no cycles.
- Use exactly `V - 1` edges, where `V` is the number of vertices.
- Have the minimum possible total edge weight among all spanning trees of the graph.

For example, suppose we have:

```
      4
A -------- B
|          |
2          3
|          |
C -------- D
     1
```

There are several ways we could connect all four vertices. An MST chooses a set of edges that keeps every vertex connected while minimizing the total cost.

---

## Spanning Tree vs Minimum Spanning Tree
A **spanning tree** connects every vertex of a graph without creating cycles.

A **minimum spanning tree** does the same thing, but additionally chooses the spanning tree with the smallest possible total edge weight.

Therefore, every MST is a spanning tree, but not every spanning tree is minimum.

---

## Why Minimum Spanning Trees Matter
MSTs are useful when we need to connect many locations while minimizing the total cost of the connections.

Examples include:

- Computer networks
- Electrical networks
- Road construction
- Telecommunications
- Pipeline networks
- Network design

Instead of finding the cheapest route between two locations, an MST attempts to connect the **entire network** as cheaply as possible.

---

## MST vs Shortest Path
Minimum Spanning Trees and shortest-path algorithms solve different problems.

Dijkstra's Algorithm finds the cheapest path from a starting vertex to other vertices.

An MST finds the cheapest collection of edges needed to connect **all vertices**.

Therefore, a shortest-path tree produced by Dijkstra is not necessarily a Minimum Spanning Tree.

---

## Prim's Algorithm
Prim's Algorithm constructs an MST by starting from one vertex and repeatedly selecting the cheapest edge that connects the current tree to a new vertex.

The general idea is:

1. Choose a starting vertex.
2. Examine edges leading to unvisited vertices.
3. Select the cheapest available edge.
4. Add the new vertex to the tree.
5. Repeat until every vertex has been included.

Prim's Algorithm is closely related to **priority queues and heaps**, because a priority queue can efficiently keep track of the cheapest available edge.

---

## Kruskal's Algorithm
Kruskal's Algorithm approaches the problem differently. Instead of starting from one vertex, it considers edges across the entire graph.

The general idea is:

1. Sort all edges from smallest weight to largest weight.
2. Select the cheapest edge.
3. Add it if doing so does not create a cycle.
4. Skip it if it would create a cycle.
5. Continue until the MST contains `V - 1` edges.

Kruskal's Algorithm is commonly implemented using a **Disjoint Set Union (Union-Find)** data structure to determine whether adding an edge would create a cycle.

---

## Prim's vs Kruskal's
Both algorithms find a Minimum Spanning Tree, but they construct it differently.

Prim's grows **one tree outward from a starting vertex** by repeatedly choosing a cheap edge connecting the tree to a new vertex.

Kruskal's considers **edges globally**, selecting the cheapest valid edges and gradually joining separate components together.

---

## Time Complexity
The exact time complexity depends on the implementation.

Prim's Algorithm using an adjacency list and binary heap commonly runs in:

`O(E log V)`

Kruskal's Algorithm is dominated by sorting the edges and commonly runs in:

`O(E log E)`

where:

`V` = number of vertices
`E` = number of edges

---

## Limitations and Important Conditions
The standard MST problem assumes the graph is **weighted, undirected, and connected**.

If the graph is disconnected, a single spanning tree connecting every vertex cannot exist. Instead, MST algorithms can produce a **minimum spanning forest**, containing a minimum spanning tree for each connected component.

A graph may also have more than one valid MST when different edge choices produce the same minimum total weight.

---

## Algorithms Covered
This folder will contain implementations and notes for:

- Prim's Algorithm
- Kruskal's Algorithm

These algorithms will later be compared in terms of runtime, memory usage, graph density, and behavior across different weighted graph structures.
