# Bellman-Ford Algorithm

## Overview

### Q1: What is Bellman-Ford?
Ans: Bellman-Ford is a single-source shortest-path algorithm that can find shortest paths even when a graph contains negative edge weights.

Unlike Dijkstra, Bellman-Ford does not greedily finalize the currently closest node.

Instead, it repeatedly performs relaxation on every edge.

Bellman-Ford can:

- Handle positive weights
- Handle zero weights
- Handle negative weights
- Detect reachable negative-weight cycles

---

### Q2: Why do we need Bellman-Ford if we already have Dijkstra?
Ans: Dijkstra assumes that edge weights are non-negative.

A negative edge can allow a path that initially looks expensive to later become cheaper.

Bellman-Ford does not make Dijkstra's greedy finalization assumption.

Instead, it repeatedly checks every edge and allows better distances to propagate through the graph.

So:

```
Dijkstra -> faster, but requires non-negative weights

Bellman-Ford -> slower, but handles negative weights
```

---

## Intuition

Suppose we have:

```
A -> B = 5
A -> C = 2
B -> D = 2
C -> B = -4
```

At first:

```
A -> B
cost = 5
```

looks like one way to reach B.

But:

```
A -> C -> B
```

costs:

```
2 + (-4) = -2
```

So:

```
dist[B] = -2
```

is better than:

```
dist[B] = 5
```

The negative edge changed what the best path looks like.

Bellman-Ford handles this by repeatedly asking:

> Can any edge give me a better distance?

---

## Relaxation

### Q3: What is relaxation?
Ans: Relaxation means checking whether traveling through one node gives us a cheaper path to another node.

For an edge:

```
u -> v
```

with weight:

```
w
```

we check:

```
dist[u] + w < dist[v]
```

If true:

```
dist[v] = dist[u] + w
```

In Python:

```python
if distance[u] + weight < distance[v]:
    distance[v] = distance[u] + weight
```

This same idea appears in:

- Dijkstra
- 0-1 BFS
- Bellman-Ford

The major difference is how and when relaxation is performed.

---

## The Core Idea

### Q4: What makes Bellman-Ford different?
Ans: Bellman-Ford relaxes every edge repeatedly.

Conceptually:

```
Round 1 -> relax every edge

Round 2 -> relax every edge

Round 3 -> relax every edge

...

Round V - 1 -> relax every edge
```

This gives shortest-path information enough opportunities to propagate through the graph.

---

## Why V - 1?

### Q5: Why does Bellman-Ford perform at most V - 1 rounds?
Ans: In a graph with V vertices, a simple path can contain at most:

```
V - 1 edges
```

Why?

Because a simple path does not repeat vertices.

Suppose we have:

```
A -> B -> C -> D
```

There are:

```
4 vertices
3 edges
```

Therefore:

```
V = 4

V - 1 = 3
```

In general:

```
Maximum edges in a simple path = V - 1
```

If no relevant negative cycle exists, a shortest path never needs to repeat a vertex.

Therefore, after enough relaxation rounds for paths of up to V - 1 edges to propagate, all shortest distances must have been found.

---

## Important Mental Model for V - 1

Think of each full relaxation round as allowing shortest-path information to potentially travel one edge farther.

After:

```
1 round
```

paths using approximately one edge can be established.

After:

```
2 rounds
```

paths using approximately two edges can be established.

And so on.

By:

```
V - 1 rounds
```

even the longest possible simple shortest path has had enough opportunity to propagate.

Note: Depending on edge-processing order, information may travel farther than one edge during a single round. V - 1 is the safe upper bound.

---

## Simple Example

Consider:

```
A -> B = 4
A -> C = 5
B -> C = -2
C -> D = 3
```

Start from:

```
A
```

Initial distances:

```
A = 0
B = infinity
C = infinity
D = infinity
```

### Relax A -> B

```
0 + 4 < infinity
```

So:

```
B = 4
```

### Relax A -> C

```
0 + 5 < infinity
```

So:

```
C = 5
```

### Relax B -> C

Current:

```
B = 4
C = 5
```

Check:

```
4 + (-2) < 5
```

which gives:

```
2 < 5
```

So:

```
C = 2
```

### Relax C -> D

```
2 + 3 < infinity
```

So:

```
D = 5
```

Final distances:

```
A = 0
B = 4
C = 2
D = 5
```

The negative edge:

```
B -> C = -2
```

caused C to become cheaper than the direct path from A.

---

## Data Structures Used

Bellman-Ford commonly uses:

- Edge list
- Distance map
- Optional parent map

An edge list might look like:

```python
edges = [
    ("A", "B", 4),
    ("A", "C", 5),
    ("B", "C", -2),
    ("C", "D", 3),
]
```

Each edge contains:

```
(source, destination, weight)
```

---

## Why an Edge List?

### Q6: Why is an edge list convenient for Bellman-Ford?
Ans: Bellman-Ford repeatedly needs to examine every edge.

An edge list makes this extremely straightforward:

```python
for u, v, weight in edges:
```

We can also use an adjacency list, but an edge list naturally matches Bellman-Ford's repeated full-edge relaxation process.

---

## Algorithm Steps

1. Set every distance to infinity.
2. Set the source distance to 0.
3. Repeat up to V - 1 times:
   - Examine every edge.
   - Relax the edge if a cheaper path is found.
4. Perform another pass over all edges.
5. If any reachable distance can still improve:
   - A reachable negative-weight cycle exists.
6. Otherwise:
   - The shortest distances are valid.

---

## Python Implementation

```python
def bellman_ford(vertices, edges, start):

    distance = {vertex: float("inf") for vertex in vertices}
    parent = {vertex: None for vertex in vertices}

    distance[start] = 0

    # Relax every edge V - 1 times
    for _ in range(len(vertices) - 1):

        updated = False

        for u, v, weight in edges:

            # Only relax from a reachable vertex
            if distance[u] != float("inf"):

                new_distance = distance[u] + weight

                if new_distance < distance[v]:

                    distance[v] = new_distance
                    parent[v] = u
                    updated = True

        # If nothing changed, shortest paths are already stable
        if not updated:
            break

    # Check for a reachable negative-weight cycle
    for u, v, weight in edges:

        if distance[u] != float("inf"):

            if distance[u] + weight < distance[v]:
                return None, None, True

    return distance, parent, False
```

---

## Example Usage

```python
vertices = ["A", "B", "C", "D"]

edges = [
    ("A", "B", 4),
    ("A", "C", 5),
    ("B", "C", -2),
    ("C", "D", 3),
]

distance, parent, negative_cycle = bellman_ford(
    vertices,
    edges,
    "A",
)

print(distance)
print(parent)
print(negative_cycle)
```

Expected distances:

```
A = 0
B = 4
C = 2
D = 5
```

And:

```
negative_cycle = False
```

---

## Code Walkthrough

### 1. Initialize Distances

```python
distance = {vertex: float("inf") for vertex in vertices}
distance[start] = 0
```

Every vertex begins unreachable except the source.

---

### 2. Repeat V - 1 Times

```python
for _ in range(len(vertices) - 1):
```

This gives shortest-path information enough opportunities to propagate across the longest possible simple path.

---

### 3. Examine Every Edge

```python
for u, v, weight in edges:
```

Unlike Dijkstra, Bellman-Ford does not choose only the currently cheapest vertex.

It repeatedly checks all edges.

---

### 4. Ignore Unreachable Starting Vertices

```python
if distance[u] != float("inf"):
```

If u cannot currently be reached from the source, we cannot use:

```
u -> v
```

to improve a source-based path.

---

### 5. Relax

```python
if new_distance < distance[v]:
```

If going through u gives us a cheaper route to v, update it.

---

### 6. Track Parents

```python
parent[v] = u
```

This allows us to reconstruct the shortest path later.

---

## Early Termination

### Q7: Do we always need all V - 1 rounds?
Ans: No.

Suppose an entire round occurs and no distance changes.

Then:

```python
updated = False
```

remains unchanged.

That means no edge can currently improve any shortest path.

The distances have stabilized.

So we can stop early:

```python
if not updated:
    break
```

This can significantly improve practical performance on some graphs.

However, the theoretical worst-case time complexity remains:

```
O(VE)
```

---

# Negative-Weight Cycles

## Q8: What is a negative-weight cycle?
Ans: A negative-weight cycle is a cycle whose total edge weight is negative.

Example:

```
A -> B = 2
B -> C = -5
C -> A = 1
```

Cycle cost:

```
2 + (-5) + 1 = -2
```

So every time we travel around the cycle:

```
cost decreases by 2
```

Go around once:

```
-2
```

Twice:

```
-4
```

Three times:

```
-6
```

And so on.

There is no finite minimum.

We can keep making the path cheaper forever.

---

## Why Negative Cycles Matter

### Q9: Why does a negative cycle cause problems for shortest paths?
Ans: Suppose reaching a destination costs:

```
10
```

But before reaching it, we can travel around a negative cycle.

After one loop:

```
8
```

After another:

```
6
```

Then:

```
4
2
0
-2
-4
...
```

There is no smallest finite value.

Therefore the shortest-path problem becomes undefined for destinations whose paths can exploit that negative cycle.

---

# Detecting Negative Cycles

### Q10: How does Bellman-Ford detect a negative cycle?
After completing up to:

```
V - 1
```

relaxation rounds, Bellman-Ford performs one additional pass.

We ask:

```
Can ANY reachable edge still be relaxed?
```

If:

```
dist[u] + weight < dist[v]
```

is still true, then a distance can continue decreasing even after paths of up to V - 1 edges should already have stabilized.

That indicates a reachable negative-weight cycle.

---

## Why Does the Extra Round Work?

Without a negative cycle, a shortest path can be represented as a simple path with at most:

```
V - 1 edges
```

Therefore after sufficient relaxation:

```
No distance should improve anymore.
```

If an improvement is still possible, some beneficial path must effectively involve repeating vertices.

Repeating vertices means a cycle exists.

If repeating that cycle lowers the path cost, it is a:

```
negative-weight cycle
```

---

## Important Detail: Reachable Negative Cycles

### Q11: Does Bellman-Ford detect every negative cycle anywhere in the graph?
Ans: Standard single-source Bellman-Ford detects negative cycles that are reachable from the chosen source.

Suppose:

```
A -> B -> C
```

and somewhere completely disconnected:

```
X -> Y -> Z -> X
```

contains a negative cycle.

If we start from:

```
A
```

then:

```
X, Y, Z
```

remain unreachable.

That disconnected negative cycle does not affect shortest paths from A.

This is why our code checks:

```python
if distance[u] != float("inf"):
```

before considering an edge during negative-cycle detection.

---

# Negative Edge vs Negative Cycle

### Q12: Is a negative edge automatically a problem?
Ans: No.

A negative edge is perfectly acceptable for Bellman-Ford.

Example:

```
A -> B = 5
B -> C = -3
```

There is nothing inherently wrong with this.

The problem occurs when a cycle has a negative total weight.

So:

```
Negative edge -> Bellman-Ford can handle it

Negative cycle -> finite shortest paths may not exist for affected nodes
```

---

# Path Reconstruction

### Q13: How do we reconstruct the shortest path?
Use the parent map.

Suppose:

```
parent[D] = C
parent[C] = B
parent[B] = A
```

Starting from D:

```
D <- C <- B <- A
```

Reverse it:

```
A -> B -> C -> D
```

Python:

```python
def reconstruct_path(parent, start, target):

    path = []
    current = target

    while current is not None:
        path.append(current)

        if current == start:
            break

        current = parent[current]

    if not path or path[-1] != start:
        return None

    path.reverse()
    return path
```

---

# Directed Graphs

### Q14: Does Bellman-Ford work on directed graphs?
Ans: Yes.

For:

```
A -> B = 5
```

the algorithm treats this as an edge from:

```
A -> B
```

only.

---

# Undirected Graphs

### Q15: Does Bellman-Ford work on undirected graphs?
Ans: Yes, but there is an important issue involving negative weights.

An undirected edge:

```
A - B = -3
```

can be represented as:

```
A -> B = -3
B -> A = -3
```

This immediately creates the cycle:

```
A -> B -> A
```

with cost:

```
-3 + (-3) = -6
```

So a negative-weight undirected edge creates a negative cycle under the standard graph model.

This means shortest paths become problematic if that edge is reachable.

---

# Disconnected Graphs

### Q16: Can Bellman-Ford handle disconnected graphs?
Ans: Yes.

Vertices unreachable from the chosen source remain:

```
infinity
```

Example:

```
A -> B -> C

D -> E
```

Starting from A:

```
A = 0
B = ...
C = ...

D = infinity
E = infinity
```

Bellman-Ford is still a single-source shortest-path algorithm.

---

# Bellman-Ford vs Dijkstra

### Dijkstra

Works with:

```
non-negative weights
```

Uses:

```
priority queue
```

Typical complexity:

```
O((V + E) log V)
```

with a binary heap and adjacency list.

Main philosophy:

> Always process the currently cheapest candidate.

---

### Bellman-Ford

Works with:

```
positive weights
zero weights
negative weights
```

Uses:

```
repeated edge relaxation
```

Complexity:

```
O(VE)
```

Main philosophy:

> Keep relaxing every edge until shortest distances have had enough opportunities to propagate.

---

## Q17: Why doesn't Bellman-Ford need a priority queue?
Ans: Bellman-Ford does not depend on greedily choosing the currently cheapest node.

It systematically revisits all edges.

Therefore it does not need Dijkstra's priority-based processing order.

---

# Why Dijkstra Fails With Negative Weights

Suppose Dijkstra believes a node has reached its final shortest distance.

Later, a path containing a negative edge could make that node cheaper.

That breaks the greedy assumption behind Dijkstra.

Bellman-Ford avoids this problem because it does not permanently finalize nodes in the same way.

It allows distances to improve repeatedly.

---

# Bellman-Ford vs 0-1 BFS

### 0-1 BFS

Allowed weights:

```
0 or 1
```

Complexity:

```
O(V + E)
```

Uses:

```
deque
```

---

### Bellman-Ford

Allowed weights:

```
positive
zero
negative
```

Complexity:

```
O(VE)
```

Uses:

```
repeated relaxation
```

If weights are only:

```
0 and 1
```

0-1 BFS is generally the more appropriate specialized algorithm.

---

# Important Limitation

Bellman-Ford's flexibility comes at a cost.

For large graphs:

```
O(VE)
```

can become expensive.

Suppose:

```
V = 100000
E = 500000
```

Repeatedly examining every edge potentially becomes enormous.

So Bellman-Ford should not automatically replace Dijkstra.

Instead:

```
Non-negative weights -> Dijkstra

Only 0/1 weights -> 0-1 BFS

Negative weights -> Bellman-Ford
```

assuming the problem fits the respective algorithm.

---

# Practical Use Cases

Bellman-Ford is useful when:

- Negative edge weights may exist
- We need to detect reachable negative cycles
- Costs can represent gains and losses
- Graph constraints prevent Dijkstra's assumptions
- We want a conceptually straightforward negative-weight shortest-path algorithm

---

# A Famous Application: Currency Arbitrage

Suppose currencies can be exchanged:

```
USD -> EUR
EUR -> GBP
GBP -> USD
```

Under a mathematical transformation of exchange rates, profitable arbitrage opportunities can be represented as negative cycles.

Bellman-Ford can therefore be adapted to detect whether such a cycle exists.

The important connection is:

```
negative cycle
        |
        v
repeating the cycle continually improves the value
```

This is conceptually similar to repeatedly traveling around a negative-weight graph cycle and lowering path cost.

---

# Complexity

### Q18: What is Bellman-Ford's time complexity?

There can be:

```
V - 1
```

rounds.

Each round examines:

```
E
```

edges.

Therefore:

```
O((V - 1)E)
```

which simplifies to:

```
O(VE)
```

---

### Q19: What is the space complexity?

For distance and parent structures:

```
O(V)
```

auxiliary space.

Graph storage using an edge list requires:

```
O(E)
```

So including graph storage:

```
O(V + E)
```

---

# Comparison

- BFS
  - Allowed weights: equal/unweighted
  - Main structure/strategy: queue
  - Typical time: O(V + E)

- 0-1 BFS
  - Allowed weights: 0 or 1
  - Main structure/strategy: deque
  - Typical time: O(V + E)

- Dijkstra
  - Allowed weights: non-negative
  - Main structure/strategy: priority queue
  - Typical time: O((V + E) log V)

- Bellman-Ford
  - Allowed weights: negative allowed
  - Main structure/strategy: repeated relaxation
  - Typical time: O(VE)

---

# When Should I Use Bellman-Ford?

Ask:

```
Do I need shortest paths?
        |
       Yes
        |
Can negative edges exist?
        |
       Yes
        |
Bellman-Ford
```

Especially if we also need:

```
negative-cycle detection
```

If all weights are non-negative:

```
Dijkstra is generally more efficient.
```

If weights are only:

```
0 or 1
```

use:

```
0-1 BFS
```

when appropriate.

---

# Key Things to Remember

### Rule 1

Bellman-Ford is a:

```
single-source shortest-path algorithm
```

---

### Rule 2

It can handle:

```
negative edge weights
```

---

### Rule 3

It repeatedly:

```
relaxes every edge
```

---

### Rule 4

Maximum standard relaxation rounds:

```
V - 1
```

because a simple path can contain at most V - 1 edges.

---

### Rule 5

After those rounds:

```
Relax every edge one more time.
```

If a reachable distance still improves:

```
reachable negative cycle exists
```

---

### Rule 6

Negative edge:

```
allowed
```

Negative cycle:

```
can destroy the existence of a finite shortest path
```

for affected destinations.

---

### Rule 7

If an entire relaxation round changes nothing:

```
stop early
```

because the distances have stabilized.

---

# Questions to Test My Understanding

Before considering Bellman-Ford complete, I should be able to answer:

## Conceptual

1. What problem does Bellman-Ford solve?
2. Why can Bellman-Ford handle negative edges while Dijkstra cannot safely do so?
3. What is relaxation?
4. Why does Bellman-Ford repeatedly examine every edge?
5. Why are V - 1 rounds sufficient?
6. Why can a simple path contain at most V - 1 edges?
7. Why might the algorithm finish before V - 1 rounds?
8. What is a negative-weight cycle?
9. Why does a negative-weight cycle cause problems for shortest paths?
10. How does the additional relaxation pass detect a negative cycle?
11. Why does standard single-source Bellman-Ford only detect negative cycles reachable from the source?
12. Is a negative edge itself a problem?
13. Can Bellman-Ford work on directed graphs?
14. What happens with a negative undirected edge?
15. What happens to unreachable vertices?
16. Why is an edge list convenient?
17. Why doesn't Bellman-Ford require a priority queue?
18. What is Bellman-Ford's time complexity?
19. How do we reconstruct the shortest path?
20. When should we choose Bellman-Ford over Dijkstra?

---

# Questions Worth Investigating During Experiments

## 1. Bellman-Ford vs Dijkstra

On graphs containing only non-negative weights:

```
How much faster is Dijkstra in practice?
```

Both should produce the same shortest distances.

But their runtime behavior should differ.

---

## 2. Graph Size

Test:

```
100 vertices
1000 vertices
5000 vertices
10000 vertices
```

How quickly does Bellman-Ford's runtime increase?

Because of:

```
O(VE)
```

we may see scaling problems much earlier than with BFS or Dijkstra.

---

## 3. Graph Density

Compare:

```
sparse graphs
vs
dense graphs
```

Since Bellman-Ford repeatedly processes every edge:

```
Does increasing E dramatically affect runtime?
```

---

## 4. Early Termination

Record:

```
maximum possible rounds
vs
actual rounds executed
```

How frequently does Bellman-Ford stabilize before reaching:

```
V - 1
```

rounds?

---

## 5. Edge Order

Because updates made earlier in a round may influence later edges in that same round:

```
Does changing edge-processing order affect the number of rounds needed in practice?
```

The final correct distances should remain the same when no reachable negative cycle affects them, but convergence speed may differ.

---

## 6. Negative Edge Frequency

Generate graphs containing:

```
0% negative edges
5% negative edges
10% negative edges
20% negative edges
```

while avoiding negative cycles where necessary.

Ask:

```
Does the number or placement of negative edges affect practical convergence?
```

---

## 7. Negative Cycle Detection

Create controlled graphs containing:

```
no negative cycle

reachable negative cycle

unreachable negative cycle
```

Does the implementation correctly distinguish between them?

---

## 8. Node and Edge Relaxations

Record:

```
number of relaxation attempts
number of successful relaxations
```

How do these values change with:

```
graph size
density
weight distribution
edge order
```

---

# Final Mental Model

Dijkstra behaves like:

> "I trust that once I select the cheapest node under non-negative weights, I can safely move forward."

Bellman-Ford behaves more cautiously:

> "I don't trust any early answer. I'll keep checking every road to see whether someone discovered a cheaper route."

So Bellman-Ford repeatedly performs:

```
RELAX
RELAX
RELAX
RELAX
```

for up to:

```
V - 1 rounds
```

Then it asks one final question:

```
Can I STILL make something cheaper?
```

If:

```
No -> shortest distances are stable.
```

If:

```
Yes -> a reachable negative-weight cycle exists.
```

The core idea to remember is:

> Bellman-Ford sacrifices speed for the ability to handle negative edges and detect reachable negative-weight cycles.
