# Multi-Source Search

## Overview

### Q1: What is Multi-Source Search?
Ans: Multi-Source Search is a search strategy where we begin from multiple source nodes simultaneously instead of starting from only one source.

Normal BFS:

```
Source A -> search outward
```

Multi-Source BFS:

```
Source A \
Source B  -> search outward simultaneously
Source C /
```

The goal is usually to find the shortest distance from every node to its nearest source.

---

### Q2: What is the main idea behind Multi-Source BFS?
Ans: Instead of running BFS separately from every source, we put all source nodes into the queue at the beginning.

Every source starts with:

```
distance = 0
```

Then normal BFS continues from all of them together.

Their search regions spread outward like multiple waves.

---

## Intuition

Imagine a city containing three hospitals:

```
Hospital A

Hospital B

Hospital C
```

We want to answer:

> How far is every neighborhood from its nearest hospital?

One approach would be:

```
Run BFS from Hospital A
Run BFS from Hospital B
Run BFS from Hospital C
Compare all results
```

But that repeats a lot of work.

Instead, Multi-Source BFS begins with:

```
Queue = [Hospital A, Hospital B, Hospital C]
```

and:

```
distance[A] = 0
distance[B] = 0
distance[C] = 0
```

All three BFS waves then spread outward simultaneously.

The first wave to reach a node gives that node its shortest distance to any source.

---

## Simple Example

Consider:

```
A - B - C - D - E - F - G
```

Suppose:

```
Sources = A and G
```

We initialize:

```
A = 0
G = 0
```

Both searches spread outward:

```
A -> B -> C -> D <- E <- F <- G
```

Distances become:

```
A = 0
B = 1
C = 2
D = 3
E = 2
F = 1
G = 0
```

Notice that each node stores its distance from the closest source, not necessarily from A.

For example:

```
F
```

is only:

```
1
```

edge away from G.

---

## Data Structures Used

Multi-Source BFS usually uses:

- Queue
- Distance map
- Optional parent map
- Optional source/owner map
- Adjacency list

Unlike Bidirectional BFS, we do not need separate queues for every source.

All sources share the same queue.

---

## Core Rule

### Q3: What is the most important rule in Multi-Source BFS?
Ans: Initialize every source with distance 0 and place every source into the queue before BFS begins.

Instead of:

```
queue = deque([start])
```

we do:

```
queue = deque(sources)
```

And instead of:

```
distance[start] = 0
```

we do:

```
for source in sources:
    distance[source] = 0
```

After initialization, the algorithm behaves almost exactly like normal BFS.

---

## Algorithm Steps

For an unweighted graph:

1. Set every node's distance to infinity.
2. Create an empty queue.
3. For every source:
   - Set its distance to 0.
   - Add it to the queue.
4. Begin BFS.
5. Pop a node from the front.
6. Examine its neighbors.
7. If a neighbor has not received a shorter distance:
   - Set its distance.
   - Record its parent if needed.
   - Add it to the queue.
8. Continue until the queue is empty.

---

## Python Implementation

```python
from collections import deque

def multi_source_bfs(graph, sources):

    distance = {node: float("inf") for node in graph}
    parent = {node: None for node in graph}

    queue = deque()

    for source in sources:
        distance[source] = 0
        queue.append(source)

    while queue:

        current = queue.popleft()

        for neighbor in graph[current]:

            if distance[neighbor] == float("inf"):

                distance[neighbor] = distance[current] + 1
                parent[neighbor] = current

                queue.append(neighbor)

    return distance, parent
```

---

## Code Walkthrough

### 1. Distance Map

```
distance = {node: float("inf") for node in graph}
```

Initially, every node is considered unreachable.

---

### 2. Add All Sources

```
for source in sources:
    distance[source] = 0
    queue.append(source)
```

This is the defining step of Multi-Source BFS.

Every source begins at BFS level 0.

---

### 3. Process the Queue

```
current = queue.popleft()
```

Just like ordinary BFS, nodes are processed in FIFO order.

---

### 4. Visit Neighbors

```
if distance[neighbor] == float("inf"):
```

If the node has not been reached yet, the current BFS wave has reached it first.

We assign:

```
distance[neighbor] = distance[current] + 1
```

Because BFS explores in increasing distance order, this is the shortest distance from that node to any source.

---

## Why Does One Queue Work?

### Q4: Why don't we need one queue for every source?
Ans: Because all sources begin at the same distance:

```
0
```

The initial queue might look like:

```
[A, G, K]
```

All three are level 0.

Their neighbors will then enter at level:

```
1
```

Then their neighbors enter at:

```
2
```

and so on.

The single FIFO queue naturally preserves the combined BFS levels.

---

## Super-Source Mental Model

### Q5: Is there another way to understand Multi-Source BFS?
Ans: Yes.

Imagine creating a fake node called:

```
SUPER SOURCE
```

and connecting it to every real source with a zero-cost conceptual edge:

```
             -> Source A
Super Source -> Source B
             -> Source C
```

Then searching outward from that super-source resembles starting from all sources simultaneously.

For ordinary unweighted Multi-Source BFS, we usually do not actually create this node.

We simply initialize all real sources at distance 0.

This is mainly a useful mental model.

---

## Source Ownership

Sometimes we want to know more than:

```
How far is this node from the nearest source?
```

We may also want:

```
WHICH source is closest?
```

For that, we can maintain an owner map.

---

## Python Implementation With Source Tracking

```python
from collections import deque

def multi_source_bfs(graph, sources):

    distance = {node: float("inf") for node in graph}
    owner = {node: None for node in graph}

    queue = deque()

    for source in sources:

        distance[source] = 0
        owner[source] = source

        queue.append(source)

    while queue:

        current = queue.popleft()

        for neighbor in graph[current]:

            if distance[neighbor] == float("inf"):

                distance[neighbor] = distance[current] + 1
                owner[neighbor] = owner[current]

                queue.append(neighbor)

    return distance, owner
```

Now we can determine:

```
Node X:

distance = 3
nearest source = A
```

---

## What If Two Sources Are Equally Close?

### Q6: What happens when a node has the same shortest distance from two sources?
Ans: The basic implementation usually assigns the node to whichever source's BFS wave reaches it first.

For example:

```
A - B - C - D - E
```

with:

```
Sources = A and E
```

Node C is:

```
2 edges from A
2 edges from E
```

So there is a tie.

Which source becomes the recorded owner can depend on:

- source insertion order
- adjacency-list order
- queue processing order

The shortest distance remains correct.

But if the application requires tracking all equally nearest sources, additional logic is needed.

---

## Multi-Source BFS vs Running BFS Multiple Times

### Q7: Why not just run BFS once for every source?
Suppose:

```
k = number of sources
```

A single BFS costs:

```
O(V + E)
```

Running BFS separately from every source costs:

```
O(k(V + E))
```

Multi-Source BFS performs one combined traversal:

```
O(V + E)
```

when the goal is to find the minimum distance to any source.

That can be a major improvement when there are many sources.

---

## Important Distinction

Multi-Source BFS answers:

> What is the distance from each node to its nearest source?

It does not automatically give us the separate distance from every node to every source.

For example, with:

```
Sources = A, B, C
```

Multi-Source BFS might tell us:

```
X is 3 edges from its nearest source.
```

But if we need:

```
Distance X -> A
Distance X -> B
Distance X -> C
```

separately, then a single standard Multi-Source BFS is not enough.

---

## Multi-Source BFS vs Bidirectional BFS

### Q8: What is the difference?
These algorithms may look similar because both start searches from multiple places.

But their goals are different.

### Bidirectional BFS

Starts from:

```
Source + Target
```

and searches:

```
Source -> -> -> <- <- <- Target
```

Goal:

```
Make the two searches meet.
```

Usually used for one specific source-target shortest path.

---

### Multi-Source BFS

Starts from:

```
Source A
Source B
Source C
...
```

and searches outward:

```
A -> ->

B -> ->

C -> ->
```

Goal:

```
Find shortest distances from the nearest source.
```

The searches are not trying to meet each other.

They are collectively exploring the graph.

---

## Multi-Source BFS vs Normal BFS

### Normal BFS

Initialization:

```
Queue = [A]

distance[A] = 0
```

Finds:

```
distance from A
```

### Multi-Source BFS

Initialization:

```
Queue = [A, B, C]

distance[A] = 0
distance[B] = 0
distance[C] = 0
```

Finds:

```
distance from nearest source
```

The actual BFS mechanics after initialization are almost identical.

---

## Weighted Graphs

### Q9: Can Multi-Source BFS handle weighted graphs?
Ans: Standard Multi-Source BFS works for unweighted graphs or graphs where every edge has the same effective cost.

If the graph has arbitrary non-negative weights, we can use:

```
Multi-Source Dijkstra
```

Instead of inserting one source into the priority queue at distance 0, insert all sources at distance 0.

Conceptually:

```
for source in sources:
    distance[source] = 0
    heappush(priority_queue, (0, source))
```

Dijkstra then proceeds normally.

---

## Multi-Source Dijkstra

### Q10: What is Multi-Source Dijkstra?
Ans: It is the weighted version of the same idea.

Normal Dijkstra:

```
One source at distance 0
```

Multi-Source Dijkstra:

```
Source A = 0
Source B = 0
Source C = 0
```

All are inserted into the priority queue initially.

The algorithm then finds the minimum weighted distance from every reachable node to its nearest source.

For a binary-weight graph, the same multi-source idea can also be combined with 0-1 BFS by initially placing every source into the deque at distance 0.

---

## Directed Graphs

### Q11: Does Multi-Source BFS work on directed graphs?
Ans: Yes.

The search simply follows the direction of the edges.

For:

```
A -> B -> C
```

a source at A can reach:

```
B
C
```

but a source at C cannot automatically travel backward to:

```
B
A
```

unless those reverse edges exist.

---

## Undirected Graphs

Multi-Source BFS also works naturally on undirected graphs.

For:

```
A - B
```

both directions are available.

No algorithm change is required.

---

## Disconnected Graphs

### Q12: Can Multi-Source BFS handle disconnected graphs?
Ans: Yes.

If a disconnected component contains no source, its nodes remain:

```
infinity
```

Example:

```
A - B - C

D - E - F
```

Suppose:

```
Sources = [A]
```

Then:

```
A = 0
B = 1
C = 2

D = infinity
E = infinity
F = infinity
```

If we instead use:

```
Sources = [A, D]
```

both components become reachable from at least one source.

---

## Path Reconstruction

### Q13: Can we reconstruct a path to the nearest source?
Ans: Yes.

Maintain a parent map just like ordinary BFS.

When:

```
parent[neighbor] = current
```

we record which node caused the neighbor to be discovered.

Starting from a target node and repeatedly following its parent eventually leads back to whichever source reached it.

Because the parent direction points toward the discovering source, the collected path can be reversed or interpreted appropriately depending on which direction we want to display it.

---

## Practical Use Cases

### Nearest Facility

Given several:

- hospitals
- police stations
- fire stations
- charging stations
- warehouses

find the nearest one for every location.

---

### Grid Problems

Suppose a grid contains several fires.

Instead of running BFS from each fire separately:

```
Fire A
Fire B
Fire C
```

start BFS from all fires simultaneously.

The resulting distance for each cell tells us:

```
How soon can fire reach this cell?
```

---

### Infection or Contamination Spread

If several locations are infected at time 0, Multi-Source BFS can model simultaneous spreading through an unweighted network.

---

### Nearest Exit

If a maze has several exits, we can start from all exits and determine the distance of every cell to its nearest exit.

---

### Voronoi-Like Graph Regions

Using an owner map, the graph can be divided into regions according to which source is closest.

Conceptually:

```
Region A -> closest to Source A

Region B -> closest to Source B

Region C -> closest to Source C
```

---

## Complexity

### Q14: What is the time complexity of Multi-Source BFS?
Ans:

```
O(V + E)
```

Even though there are multiple sources, each vertex and edge still needs to be processed only a constant number of times in the standard traversal.

---

### Q15: What is the space complexity?
Auxiliary space:

```
O(V)
```

for structures such as:

- queue
- distance
- parent
- owner

Including adjacency-list graph storage:

```
O(V + E)
```

---

## Comparison

- BFS
  - Sources: one
  - Edge weights: unweighted
  - Main purpose: distance from one source

- Multi-Source BFS
  - Sources: multiple
  - Edge weights: unweighted
  - Main purpose: distance from nearest source

- 0-1 BFS
  - Sources: one
  - Edge weights: 0 or 1
  - Main purpose: binary-weight shortest path

- Multi-Source 0-1 BFS
  - Sources: multiple
  - Edge weights: 0 or 1
  - Main purpose: binary-weight distance from nearest source

- Dijkstra
  - Sources: one
  - Edge weights: non-negative
  - Main purpose: weighted shortest path

- Multi-Source Dijkstra
  - Sources: multiple
  - Edge weights: non-negative
  - Main purpose: weighted distance from nearest source

- Bidirectional BFS
  - Sources: source + target
  - Edge weights: unweighted
  - Main purpose: one-to-one shortest path

---

## When Should I Use Multi-Source Search?

Ask:

```
Do I have multiple starting locations?
        |
       Yes
        |
Do I want the minimum distance to ANY source?
        |
       Yes
        |
Are edges unweighted/equal cost?
        |
       Yes
        |
Multi-Source BFS
```

If edges have arbitrary non-negative weights:

```
Multi-Source Dijkstra
```

If edges only have weights 0 and 1:

```
Multi-Source 0-1 BFS
```

---

## Important Limitations

Multi-Source BFS is not automatically appropriate when:

- We need distances to each source separately.
- Edge weights differ.
- We need a specific source-target search where Bidirectional Search would be more appropriate.
- The graph contains weighted costs that ordinary BFS cannot represent.

The key question is:

> Do I want the shortest distance to any one of several sources?

If yes, Multi-Source Search is worth considering.

---

## Questions to Test My Understanding

Before considering Multi-Source Search complete, I should be able to answer:

### Conceptual

1. What is Multi-Source Search?
2. What changes between normal BFS and Multi-Source BFS?
3. Why are all sources initialized with distance 0?
4. Why can all sources share one queue?
5. Why does the first BFS wave reaching a node give its minimum distance to any source?
6. What does the super-source mental model represent?
7. What is the purpose of an owner map?
8. What happens when two sources are equally close to a node?
9. Why is one Multi-Source BFS potentially better than running BFS separately from every source?
10. Does Multi-Source BFS give separate distances to every source?
11. What is the difference between Multi-Source BFS and Bidirectional BFS?
12. Can Multi-Source BFS handle directed graphs?
13. What happens to a disconnected component containing no source?
14. Can Multi-Source BFS handle weighted graphs?
15. What is Multi-Source Dijkstra?
16. Can the same idea be applied to 0-1 BFS?
17. How would we reconstruct a path from a node to its nearest source?

---

## Questions Worth Investigating During Experiments

### 1. Multi-Source BFS vs Repeated BFS

Compare:

```
Run BFS separately from every source
```

against:

```
One Multi-Source BFS
```

How does runtime change as the number of sources increases?

---

### 2. Number of Sources

Test:

```
1 source
5 sources
10 sources
50 sources
100 sources
```

How does increasing the number of sources affect:

```
runtime
memory
average nearest-source distance
```

---

### 3. Graph Density

Does Multi-Source BFS behave differently on:

```
sparse graphs
vs
dense graphs
```

---

### 4. Source Placement

Compare sources that are:

```
clustered together
```

against sources that are:

```
spread across the graph
```

How does placement affect the number of levels explored before the graph is covered?

---

### 5. Disconnected Graphs

What happens when:

```
some components contain sources
some components contain no sources
```

Can the algorithm correctly identify unreachable regions?

---

### 6. Multi-Source BFS vs Multi-Source Dijkstra

On graphs where all weights are 1, both should produce equivalent shortest distances.

How do their runtimes compare?

---

### 7. Ownership Distribution

If sources are randomly placed:

```
How many nodes become associated with each source?
```

Does graph structure cause some sources to control much larger regions than others?

---

## Final Mental Model

Normal BFS is like dropping one stone into a lake:

```
        Source
          |
          v
       ~~~~~~~
     ~~~~~~~~~~~
```

One wave spreads outward.

Multi-Source BFS is like dropping several stones at the same time:

```
Source A       Source B       Source C
   |              |              |
   v              v              v
~~~~~~~        ~~~~~~~        ~~~~~~~
```

All waves expand simultaneously.

When a wave reaches a node first, that node has found its shortest distance to the nearest source.

The key implementation difference from ordinary BFS is surprisingly small:

```
for source in sources:
    distance[source] = 0
    queue.append(source)
```

After that:

> It is essentially BFS with multiple starting points.
