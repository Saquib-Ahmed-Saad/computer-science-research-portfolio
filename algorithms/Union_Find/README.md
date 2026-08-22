# Union-Find (Disjoint Set Union)

## Overview
Union-Find, also called **Disjoint Set Union (DSU)**, is a data structure used to keep track of separate groups of connected elements.

Its main purpose is to efficiently answer two questions:

**Find:** Which group does this element belong to?

**Union:** Can two different groups be combined into one?

This makes Union-Find particularly useful for problems involving **connected components** and **cycle detection**.

---

## Intuition
Suppose we begin with five separate nodes:

```
A     B     C     D     E
```

Initially, each node belongs to its own set:

```
{A}  {B}  {C}  {D}  {E}
```

If we connect A and B:

```
A --- B

C     D     E
```

Union-Find can combine their sets:

```
{A, B}  {C}  {D}  {E}
```

If we later connect C and D:

```
A --- B

C --- D

E
```

we now have:

```
{A, B}  {C, D}  {E}
```

Finally, connecting B and C combines the first two groups:

```
A --- B --- C --- D

E
```

Union-Find now recognizes A, B, C, and D as members of the same connected component.

---

## The Two Main Operations

### Find
`Find(x)` determines which set an element belongs to by finding the **representative**, or root, of that set.

For example:

```
    A
   / \
  B   C
      |
      D
```

If A is the representative:

```
Find(B) → A
Find(C) → A
Find(D) → A
```

Since B, C, and D have the same representative, Union-Find knows they belong to the same set.

---

### Union
`Union(x, y)` combines the sets containing `x` and `y`.

Suppose:

```
A --- B

C --- D
```

There are currently two sets:

```
{A, B}

{C, D}
```

Calling:

```
Union(B, C)
```

combines them into:

```
{A, B, C, D}
```

---

## How Union-Find Detects Cycles
Union-Find can determine whether adding an edge would create a cycle.

Suppose:

```
A --- B --- C
```

Now we consider adding:

```
A --- C
```

Before adding the edge, we check:

```
Find(A)
Find(C)
```

If both return the **same representative**, A and C are already connected.

Adding another edge between them would therefore create:

```
A ----- B
 \     /
  \   /
    C
```

which contains a cycle.

This property is particularly important in **Kruskal's Algorithm**.

---

## Union-Find and Kruskal's Algorithm
Kruskal's Algorithm considers edges from smallest weight to largest weight.

Before accepting an edge between two vertices, it uses Union-Find to determine whether those vertices already belong to the same connected component.

If:

```
Find(A) != Find(B)
```

the vertices belong to different components, so the edge can be added and the sets are joined using `Union()`.

If:

```
Find(A) == Find(B)
```

the vertices are already connected, so adding the edge would create a cycle and the edge is rejected.

---

## Path Compression
A basic Union-Find structure can become inefficient if its trees become very deep.

For example:

```
A
|
B
|
C
|
D
|
E
```

Finding the root of E requires following several parent relationships.

**Path compression** shortens this path when `Find()` is performed. Nodes encountered along the way are connected more directly to the root.

The structure can gradually become closer to:

```
    A
 / / \ \
B C   D E
```

Future `Find()` operations then become much faster.

---

## Union by Rank
Another optimization is **Union by Rank**.

When combining two sets, instead of attaching either tree randomly, the smaller or shallower tree is attached beneath the larger tree.

This prevents unnecessarily deep trees from forming.

Path compression and Union by Rank together make Union-Find extremely efficient.

---

## Time Complexity
With both **path compression** and **Union by Rank**, Union-Find operations run in approximately:

```
O(α(n))
```

where `α(n)` is the inverse Ackermann function.

The inverse Ackermann function grows extremely slowly, so for practical input sizes Union-Find operations behave almost like constant time.

---

## Applications
Union-Find is commonly used for connected-component problems, cycle detection in undirected graphs, network connectivity, and Kruskal's Minimum Spanning Tree Algorithm.

It is particularly useful when connections are being added over time and we repeatedly need to determine whether two elements already belong to the same group.

---


