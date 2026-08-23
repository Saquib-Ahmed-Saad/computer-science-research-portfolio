# Bidirectional Search

## Overview

### Q1: What is Bidirectional Search?
Ans: Bidirectional Search is a search strategy that searches from both the source and the target at the same time.

Instead of searching:

- Source -> Target
we search:

- Source -> Middle
- Target -> Middle
When the two searches meet, we can combine them to construct the complete path.

---

### Q2: What is the main idea behind Bidirectional Search?
Ans: If we already know both the starting node and the target node, we may not need to search the entire distance from only one side.

Instead of:

```
A -> -> -> -> -> -> Z
```
we can do:

```
A -> -> -> M <- <- <- Z
```
where `M` is where the two searches meet.

The goal is to reduce how much of the graph needs to be explored.

---

## Intuition

### Q3: Why can Bidirectional Search be faster than normal BFS?
Ans: The important advantage comes from how search trees grow.

Suppose:

- `b` = branching factor
- `d` = distance from source to target
A normal BFS may explore roughly:

```
O(b^d)
```
nodes in a simplified search-tree model.

Bidirectional BFS searches approximately halfway from each direction:

```
O(b^(d/2))
```
from the source and:

```
O(b^(d/2))
```
from the target.

So the total is approximately:

```
O(2 * b^(d/2))
```
which is normally written as:

```
O(b^(d/2))
```
This can be dramatically smaller than:

```
O(b^d)
```
The improvement is therefore potentially much greater than simply "twice as fast."

---

## Simple Example
Consider:

```
A - B - C - D - E - F - G
```
We want the shortest path from:

```
A -> G
```
Normal BFS starts at `A`:

```
A
A -> B
A -> B -> C
A -> B -> C -> D
...
```
Bidirectional BFS starts from both sides:

```
Forward:

A -> B -> C -> D

Backward:

G -> F -> E -> D
```
The searches meet at:

```
D
```
We can then combine the two sides:

```
A -> B -> C -> D -> E -> F -> G
```

---

## Data Structures Used
For Bidirectional BFS, we usually maintain separate information for each direction.

- Forward queue
- Backward queue
- Forward visited set
- Backward visited set
- Forward parent map
- Backward parent map
Conceptually:

```
Source Search                  Target Search

Queue                          Queue
Visited                        Visited
Parent                         Parent
   |                              |
   v                              v
   -> -> -> -> meeting node <- <- <- <-
```

---

## Core Rule

### Q4: How do we know when the searches meet?
Ans: After discovering a node from one direction, check whether that node has already been discovered by the opposite search.

For example:

```
if neighbor in backward_visited:
    # The searches have met
```
or from the other direction:

```
if neighbor in forward_visited:
    # The searches have met
```
Once the searches intersect under a correct bidirectional BFS procedure, we can reconstruct the path.

---

## Algorithm Steps
For an unweighted graph:

1. Start one BFS from the source.
2. Start another BFS from the target.
3. Maintain separate queues and visited sets.
4. Expand nodes from the forward search.
5. Expand nodes from the backward search.
6. Check whether the two explored regions intersect.
7. When they meet, identify the meeting node.
8. Reconstruct the source-to-meeting path.
9. Reconstruct the meeting-to-target path.
10. Combine them.

---

## Python Implementation

```python
from collections import deque

def bidirectional_bfs(graph, start, target):

    if start == target:
        return [start]

    forward_queue = deque([start])
    backward_queue = deque([target])

    forward_visited = {start}
    backward_visited = {target}

    forward_parent = {start: None}
    backward_parent = {target: None}

    while forward_queue and backward_queue:

        # Expand one complete level from the forward side
        meeting = expand_level(
            graph,
            forward_queue,
            forward_visited,
            backward_visited,
            forward_parent
        )

        if meeting is not None:
            return build_path(
                meeting,
                forward_parent,
                backward_parent
            )

        # Expand one complete level from the backward side
        meeting = expand_level(
            graph,
            backward_queue,
            backward_visited,
            forward_visited,
            backward_parent
        )

        if meeting is not None:
            return build_path(
                meeting,
                forward_parent,
                backward_parent
            )

    return None
```
Helper function:

```python
def expand_level(
    graph,
    queue,
    own_visited,
    other_visited,
    parent
):

    level_size = len(queue)

    for _ in range(level_size):

        current = queue.popleft()

        for neighbor in graph[current]:

            if neighbor not in own_visited:

                own_visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

                if neighbor in other_visited:
                    return neighbor

    return None
```
Path reconstruction:

```python
def build_path(
    meeting,
    forward_parent,
    backward_parent
):

    path = []

    current = meeting

    while current is not None:
        path.append(current)
        current = forward_parent[current]

    path.reverse()

    current = backward_parent[meeting]

    while current is not None:
        path.append(current)
        current = backward_parent[current]

    return path
```

---

## Code Walkthrough

### 1. Two queues

```
forward_queue
backward_queue
```
The forward queue searches from the source.

The backward queue searches from the target.

---

### 2. Two visited sets

```
forward_visited
backward_visited
```
They record which vertices each search has discovered.

They also allow us to detect intersection between the searches.

---

### 3. Two parent maps

```
forward_parent
backward_parent
```
These allow us to reconstruct both halves of the final path.

---

### 4. Expand a complete BFS level
The helper function processes:

```
level_size = len(queue)
```
nodes.

This preserves BFS's level-by-level behavior rather than arbitrarily processing a single node from one side.

---

### 5. Detect intersection
When a newly discovered node exists in the opposite visited set:

```
if neighbor in other_visited:
```
the two search regions have connected.

That node becomes a possible meeting point.

---

## Path Reconstruction

### Q5: Why do we need two parent maps?
Ans: Because the two searches came from different directions.

Suppose they meet at:

```
D
```
Forward parents might represent:

```
A -> B -> C -> D
```
Backward parents might represent:

```
G -> F -> E -> D
```
The backward parent relationships point toward the target search's origin.

So we reconstruct:

```
A -> B -> C -> D
```
and then follow the backward parents:

```
D -> E -> F -> G
```
giving:

```
A -> B -> C -> D -> E -> F -> G
```

---

## Why Expand by Level?

### Q6: Why should Bidirectional BFS preserve BFS levels?
Ans: BFS guarantees shortest paths in unweighted graphs because vertices are explored in increasing distance from the source.

Bidirectional BFS must preserve that same principle from both directions.

If we expand the searches carelessly and stop at an arbitrary first intersection, reasoning about shortest-path correctness becomes harder and some implementations can return a non-shortest connection.

A clean implementation therefore expands complete BFS layers and checks for intersections systematically.

---

## Expanding the Smaller Frontier

### Q7: Do we have to alternate forward, backward, forward, backward?
Ans: No.

A common optimization is to expand whichever frontier is currently smaller.

For example:

```
if len(forward_queue) <= len(backward_queue):
    # expand forward
else:
    # expand backward
```
Why?

If one side suddenly branches into many vertices while the other side remains small, expanding the smaller frontier can reduce the amount of work.

This is often more efficient than blindly alternating sides.

However, shortest-path correctness must still be preserved by processing appropriate BFS layers and using a correct stopping condition.

---

## Complexity

### Q8: What is the time complexity?
Ans: 

For ordinary BFS:

```
O(V + E)
```
is the standard graph-based worst-case bound.

Bidirectional BFS also has a worst-case bound of:

```
O(V + E)
```
because in the worst case it may still examine a large portion of the graph.

However, its practical/search-tree advantage is often described using:

```
O(b^(d/2))
```
compared with approximately:

```
O(b^d)
```
for one-directional BFS.

Where:

- `b` = branching factor
- `d` = source-to-target distance
This explains why Bidirectional Search can provide a major practical improvement even though both algorithms may share the same graph-based worst-case bound.

---

### Q9: What is the space complexity?
Ans:

Bidirectional BFS stores:

- two frontiers
- two visited sets
- two parent maps
Worst-case space is still:

```
O(V)
```
excluding graph storage.

Including an adjacency-list graph:

```
O(V + E)
```

---

## Directed Graphs

### Q10: Does Bidirectional Search work on directed graphs?
Ans: Yes, but backward search requires special care.

Suppose the graph contains:

```
A -> B -> C -> D
```
If we start backward from `D`, we cannot simply follow `D`'s outgoing edges.

We need to discover vertices that can reach `D`.

Therefore the backward search should operate on the reverse graph.

Original graph:

```
A -> B
B -> C
C -> D
```
Reverse graph:

```
B -> A
C -> B
D -> C
```
The forward search uses the original graph.

The backward search uses the reversed graph.

---

## Undirected Graphs

### Q11: Why is Bidirectional Search easier on undirected graphs?
Ans: In an undirected graph:

```
A - B
```
means movement is possible in both directions.

Therefore the same adjacency structure can be used by both searches.

No separate reversed graph is required.

---

## Weighted Graphs

### Q12: Can Bidirectional BFS handle weighted graphs?
Ans: Standard Bidirectional BFS is intended for unweighted graphs or graphs where every edge has the same effective cost.

For weighted graphs, we cannot simply run two ordinary BFS searches.

For non-negative weighted graphs, a related algorithm is:

```
Bidirectional Dijkstra
```
The same high-level idea remains:

```
Source -> -> Middle <- <- Target
```
but each direction uses Dijkstra-style distance ordering rather than ordinary BFS queues.

The stopping condition is also more subtle than simply stopping at the first vertex seen from both sides.

---

## Bidirectional BFS vs Normal BFS

### Normal BFS

```
Source -> -> -> -> -> -> Target
```
Advantages:

- Simple
- Only one search state
- Does not require searching backward from a known target
Disadvantage:

- May explore a very large frontier before reaching a distant target

### Bidirectional BFS

```
Source -> -> -> <- <- <- Target
```
Advantages:

- Can dramatically reduce the explored search space
- Especially useful when branching factor and source-target distance are large
Disadvantages:

- Requires a known target
- Requires extra bookkeeping
- Backward traversal may be difficult
- Path reconstruction is more complicated

---

## When Bidirectional Search Is Useful
Bidirectional Search is especially attractive when:

- We know exactly one source and one target.
- The graph is large.
- The target is relatively far from the source.
- Branching factor is high.
- Searching backward from the target is possible.
- We need a shortest path in an unweighted/equal-cost graph.

---

## When Bidirectional Search May Not Help

### Q13: When might normal BFS be better?
Ans:

Bidirectional Search may provide little benefit when:

- The target is very close to the source.
- The graph is very small.
- Backward traversal is difficult or expensive.
- We want paths from one source to many/all destinations.
- There is no specific target.
- One side of the graph has an extremely unfavorable branching structure.
The additional bookkeeping may not be worthwhile for small or simple searches.

---

## Bidirectional Search vs Multi-Source Search
These concepts should not be confused.

### Bidirectional Search
Starts from:

```
Source AND Target
```
Goal:

```
Make the searches meet.
```
Example:

```
A -> -> -> <- <- <- Z
```

### Multi-Source Search
Starts from:

```
Source A
Source B
Source C
...
```
simultaneously.

Goal:

```
Find distances/reachability relative to multiple starting locations.
```
Multi-Source Search is our next topic.

---

## Important Limitation
Bidirectional Search requires us to know:

```
START
```
and:

```
TARGET
```
before beginning the search.

If the question is:

```
Find the shortest distance from A to every other vertex.
```
Bidirectional Search is generally not the appropriate tool.

There is no single destination from which to begin the backward search.

---

## Practical Intuition
Imagine two people trying to find each other in a maze.

### Normal Search
One person stays still.

The other searches:

```
Person A -> -> -> -> -> Person B
```

### Bidirectional Search
Both search:

```
Person A -> -> -> <- <- <- Person B
```
If both can navigate the maze intelligently, they may meet much sooner than if only one person searches the entire distance.

---

## Comparison

- BFS
    - Starting points: one
    - Typical use: unweighted shortest paths

- 0-1 BFS
    - Starting points: one
    - Typical use: binary-weight shortest paths

- Bidirectional BFS
    - Starting points: source + target
    - Typical use: one-to-one unweighted shortest path

- Dijkstra
    - Starting points: one
    - Typical use: non-negative weighted shortest paths

- Bidirectional Dijkstra
    - Starting points: source + target
    - Typical use: one-to-one weighted shortest path

---

## Questions to Test My Understanding
Before considering Bidirectional Search complete, I should be able to answer:

### Conceptual

1. What is Bidirectional Search?
2. Why can it be significantly faster than ordinary BFS?
3. Why is the improvement potentially much greater than simply cutting the work in half?
4. What are the forward and backward frontiers?
5. How do we know when the searches have met?
6. Why do we need two visited sets?
7. Why do we need two parent maps?
8. How do we reconstruct the final path?
9. Why should BFS levels be preserved?
10. Why might expanding the smaller frontier improve performance?
11. Does Bidirectional Search require a known target?
12. Why is it easy to search backward in an undirected graph?
13. Why do directed graphs require reversed edges for the backward search?
14. Can ordinary Bidirectional BFS handle arbitrary weighted graphs?
15. What is Bidirectional Dijkstra?
16. When might normal BFS actually be preferable?
17. What is the difference between Bidirectional Search and Multi-Source Search?

---

## Questions Worth Investigating During Experiments

### 1. BFS vs Bidirectional BFS
For the same source and target:

```
How many vertices does each algorithm explore?
```

---

### 2. Source-Target Distance
As the distance between source and target increases:

```
Does Bidirectional BFS's advantage become larger?
```

---

### 3. Branching Factor
If each node has increasingly many neighbors:

```
How quickly does ordinary BFS's explored region grow compared with Bidirectional BFS?
```

---

### 4. Graph Size
Test graphs with:

```
100
1,000
10,000
100,000
```
vertices.

Does the performance gap increase with graph size?

---

### 5. Runtime
Measure:

```
BFS runtime
vs
Bidirectional BFS runtime
```
Do fewer explored vertices consistently translate into lower runtime?

---

### 6. Memory
Bidirectional BFS maintains two sets of search structures.

So ask:

```
Does exploring shallower regions compensate for maintaining two frontiers and two visited sets?
```

---

### 7. Frontier Strategy
Compare:

```
strict alternation
```
against:

```
expand smaller frontier
```
Does choosing the smaller frontier produce a measurable improvement?

---

## Final Mental Model
Think of ordinary BFS as:

```
One army leaves Castle A
and searches all the way for Castle B.

A -> -> -> -> -> -> -> B
```
Bidirectional Search sends scouts from both castles:

```
A -> -> -> MEET <- <- <- B
```
They do not need either army to cross the entire search space.

They only need the two explored regions to connect.

The mathematical intuition is:

```
One-direction search:

approximately b^d
```
versus:

```
Two-direction search:

approximately 2 * b^(d/2)
```
The key idea to remember is:

> If both the source and target are known and we can search efficiently from both directions, meeting in the middle can dramatically reduce the search space.
