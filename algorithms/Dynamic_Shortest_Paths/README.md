# Dynamic Shortest Paths

## Overview

### Q1: What are Dynamic Shortest Paths?
Ans: Dynamic Shortest Paths refers to the problem of maintaining shortest-path information when a graph changes over time.

Until now, most shortest-path algorithms we studied assume a static graph:

```
Build graph
    |
    v
Run algorithm
    |
    v
Get shortest paths
```

But real graphs may change:

```
Edge added
Edge removed
Edge weight increased
Edge weight decreased
```

Dynamic shortest-path techniques ask:

> Can we update the existing shortest-path information without recomputing everything from scratch?

---

### Q2: Why do we care about dynamic graphs?
Ans: Many real networks are not static.

Examples include:

- Roads opening or closing
- Traffic changing travel costs
- Network links failing
- New communication links appearing
- Robot environments changing
- Game maps changing
- Social networks gaining or losing connections

Suppose we calculate:

```
A -> B -> C -> D
```

as the shortest path.

Then:

```
B -> C
```

is removed.

Our previous answer may no longer be valid.

We now need to update it.

---

# Static vs Dynamic Shortest Paths

## Static Shortest Paths

The graph remains unchanged while we solve the problem.

Example:

```
Graph
  |
  v
Dijkstra
  |
  v
Shortest distances
```

If the graph changes later, a simple approach is:

```
Run Dijkstra again.
```

---

## Dynamic Shortest Paths

We maintain information while updates occur:

```
Initial Graph
     |
     v
Shortest Paths
     |
     v
Graph Update
     |
     v
Update Shortest Paths
     |
     v
Another Update
     |
     v
Update Again
```

The goal is to avoid unnecessary recomputation.

---

# The Core Question

Suppose:

```
A -> B = 2
B -> D = 3
A -> C = 5
C -> D = 5
```

Initially:

```
A -> B -> D
```

costs:

```
2 + 3 = 5
```

while:

```
A -> C -> D
```

costs:

```
5 + 5 = 10
```

So the shortest path is:

```
A -> B -> D
cost = 5
```

Now imagine:

```
B -> D
```

changes from:

```
3
```

to:

```
20
```

Our old shortest path now costs:

```
2 + 20 = 22
```

The alternative costs:

```
10
```

So the shortest path changes to:

```
A -> C -> D
```

Dynamic shortest paths asks:

> How can we update this information efficiently after the edge changes?

---

# Types of Dynamic Problems

There are three major categories.

## 1. Incremental

### Q3: What is an incremental shortest-path problem?
Ans: The graph only receives certain additions or improving updates.

A common example is:

```
Edges are added
```

Conceptually:

```
Original graph

A -> B -> C

Update:

A -> D

New graph:

A -> B -> C
|
v
D
```

The algorithm maintains shortest-path information as new edges appear.

Depending on the exact problem definition, incremental settings may also consider particular weight decreases.

---

## 2. Decremental

### Q4: What is a decremental shortest-path problem?
Ans: The graph only receives removals or worsening updates.

Common examples:

```
Edges removed
```

or in some formulations:

```
Edge weights increase
```

Example:

```
A -> B -> C
```

then:

```
B -> C removed
```

Any shortest path depending on that edge may need to be repaired.

---

## 3. Fully Dynamic

### Q5: What is a fully dynamic shortest-path problem?
Ans: A fully dynamic problem allows both kinds of changes.

For example:

```
Edge added
Edge removed
Weight increased
Weight decreased
```

This is the most general dynamic setting.

Conceptually:

```
Graph
 |
 +-> Add edge
 |
 +-> Remove edge
 |
 +-> Change weight
 |
 v
Maintain shortest paths
```

---

# Types of Shortest-Path Queries

Dynamic shortest-path problems can also differ by what shortest paths we need to maintain.

## Single-Source Shortest Paths

```
One source -> all reachable destinations
```

Example:

```
A -> everyone
```

---

## Single-Pair Shortest Path

```
One source -> one target
```

Example:

```
A -> Z
```

---

## All-Pairs Shortest Paths

```
Every source -> every destination
```

This maintains shortest-path information between all pairs of vertices.

Dynamic all-pairs shortest paths can be significantly more complicated and expensive.

---

# What Can Change?

### Q6: What kinds of graph updates can affect shortest paths?
Four common updates are:

```
1. Edge insertion
2. Edge deletion
3. Edge-weight decrease
4. Edge-weight increase
```

Each affects the graph differently.

---

# Edge Insertion

Suppose:

```
A -> B = 5
B -> D = 5

A -> C = 10
C -> D = 10
```

Shortest path:

```
A -> B -> D
cost = 10
```

Now insert:

```
A -> D = 2
```

The new shortest path becomes:

```
A -> D
cost = 2
```

An inserted edge may create a new shortcut.

---

# Edge Deletion

Suppose:

```
A -> B -> C -> D
```

is the shortest path.

Now delete:

```
B -> C
```

The old shortest path becomes invalid.

We must find an alternative.

---

# Weight Decrease

Suppose:

```
A -> B = 10
```

changes to:

```
A -> B = 2
```

Paths using:

```
A -> B
```

may suddenly become better than previously known paths.

This resembles the propagation of a newly discovered improvement.

---

# Weight Increase

Suppose:

```
A -> B = 2
```

changes to:

```
A -> B = 50
```

If the old shortest path used this edge, that path may no longer be optimal.

We may need to find an alternative route.

---

# Not Every Update Matters

### Q7: Does every graph update change the shortest path?
Ans: No.

Suppose the shortest path is:

```
A -> B -> D
```

and we change an unrelated edge:

```
X -> Y
```

The shortest path from:

```
A -> D
```

may remain completely unchanged.

This is one of the main motivations behind dynamic algorithms.

Instead of recomputing everything, we would like to determine:

```
Which distances could actually be affected?
```

---

# Basic Approach: Recompute Everything

### Q8: What is the simplest way to handle a graph update?
Ans: Run the shortest-path algorithm again.

For example:

```
Graph changes
     |
     v
Run Dijkstra again
     |
     v
New shortest paths
```

This is called recomputation from scratch.

There is nothing incorrect about this approach.

In many applications it may actually be the best practical choice.

The dynamic question is whether we can do better.

---

# Why Recomputing Can Be Wasteful

Suppose our graph has:

```
1000000 vertices
```

and one edge changes:

```
X -> Y
```

If only a tiny region is affected, recomputing shortest paths across the entire graph may repeat enormous amounts of work.

Dynamic methods attempt to reuse information from the previous solution.

---

# Reusing Previous Information

### Q9: What information might a dynamic shortest-path method maintain?
Depending on the method, it might preserve information such as:

- Current distances
- Parent/predecessor relationships
- Shortest-path tree
- Priority information
- Affected vertices
- Alternative paths
- Additional auxiliary structures

Then, when an update occurs, it attempts to repair only what is necessary.

---

# Shortest-Path Tree

Suppose Dijkstra from A produced:

```
        A
       / \
      B   C
     / \
    D   E
```

This represents one shortest-path tree rooted at:

```
A
```

Now suppose an edge not used by the tree changes.

The current shortest paths may remain valid.

But if a tree edge changes:

```
B -> D
```

then D and potentially vertices whose shortest paths depend on D may be affected.

The tree gives us information about dependency between shortest paths.

---

# Local vs Global Effects

### Q10: Why is dynamic shortest-path maintenance difficult?
Ans: Because a tiny local graph change can sometimes have a large global effect.

Consider a bridge-like edge:

```
Large Region A
      |
      v
   X -> Y
      |
      v
Large Region B
```

If:

```
X -> Y
```

is removed, shortest paths to a huge number of vertices may change.

So:

```
Small graph update
```

does not necessarily mean:

```
Small shortest-path update
```

This is one of the central difficulties of dynamic graph algorithms.

---

# A Simple Update Idea

Suppose we already know:

```
dist[A] = 0
dist[B] = 5
dist[C] = 10
```

Now a new edge appears:

```
A -> C = 2
```

We immediately know:

```
0 + 2 < 10
```

so:

```
dist[C] = 2
```

But the effect may continue.

If:

```
C -> D = 3
```

then:

```
dist[D]
```

might also improve.

Then nodes reachable through D might improve.

So a local update can create a wave of relaxations through part of the graph.

This should feel familiar from:

```
Dijkstra
Bellman-Ford
0-1 BFS
```

because relaxation remains a fundamental shortest-path idea.

---

# Dynamic Dijkstra-Like Thinking

For graphs with non-negative weights, one conceptual strategy after a distance-improving update is:

```
Find vertices whose distances might improve
        |
        v
Place affected candidates into priority queue
        |
        v
Propagate improvements outward
```

Instead of:

```
Start Dijkstra completely from scratch
```

we attempt to begin from the region affected by the update.

However, real dynamic shortest-path algorithms require careful correctness logic, especially for deletions and weight increases.

---

# Why Deletions Can Be Harder

### Q11: Why can edge deletion be harder than edge insertion?
Ans: An insertion often gives us a new possible route.

We can ask:

```
Does this new route improve anything?
```

If not:

```
Done.
```

But deletion can destroy an existing shortest path.

Suppose:

```
A -> B -> C -> D
```

is the shortest path and:

```
B -> C
```

disappears.

We now need to determine:

```
Which nodes depended on this edge?
```

and:

```
What are their next-best alternatives?
```

The previous optimal information has been invalidated.

---

# Weight Decrease vs Weight Increase

A similar intuition applies to changing weights.

## Weight Decrease

```
Old weight = 10
New weight = 2
```

Question:

```
Does this create better paths?
```

If yes, improvements can propagate outward.

---

## Weight Increase

```
Old weight = 2
New weight = 10
```

Question:

```
Did any current shortest path depend on this cheap edge?
```

If yes, those paths may need to be repaired.

So:

```
Decrease -> potentially introduce improvements

Increase -> potentially invalidate existing optimum
```

---

# Dynamic Shortest Paths Is Not One Algorithm

### Q12: Is there a single "Dynamic Shortest Path Algorithm"?
Ans: No.

This is extremely important.

Dynamic shortest paths is a research area/problem family, not one universal algorithm like BFS or Dijkstra.

Different algorithms exist depending on:

```
Directed vs undirected

Weighted vs unweighted

Single-source vs all-pairs

Incremental vs decremental vs fully dynamic

Exact vs approximate

Graph structure
```

So when someone says:

```
dynamic shortest paths
```

the next question should be:

> What kind of dynamic shortest-path problem?

---

# Exact vs Approximate Dynamic Shortest Paths

### Q13: Do dynamic algorithms always maintain exact shortest paths?
Ans: No.

Some methods maintain:

```
Exact shortest paths
```

while others maintain:

```
Approximate shortest paths
```

Approximation may allow much faster updates.

For example, instead of guaranteeing:

```
distance = exact optimum
```

an algorithm may guarantee that the returned distance is within some controlled approximation factor.

This creates a tradeoff:

```
Accuracy <-> Update Speed
```

---

# Update Time

### Q14: What is update time?
Ans: Update time measures how much work is required when the graph changes.

For example:

```
Insert edge
     |
     v
How long until shortest-path information is updated?
```

This is different from the runtime of a static shortest-path computation.

Dynamic graph research often studies:

```
Update time
Query time
Preprocessing time
Space
```

---

# Query Time

### Q15: What is query time?
Ans: Query time measures how long it takes to answer a shortest-path question after maintaining the dynamic data structure.

Example:

```
What is the distance from A to Z?
```

A dynamic algorithm may spend more time maintaining information during updates so that later queries can be answered quickly.

This introduces another tradeoff:

```
More update work
        <->
Faster queries
```

---

# Preprocessing

Some dynamic methods first perform substantial work on the original graph.

This is called:

```
preprocessing
```

Conceptually:

```
Initial Graph
     |
     v
Expensive Preprocessing
     |
     v
Dynamic Data Structure
     |
     +-> Update
     |
     +-> Query
     |
     +-> Update
     |
     +-> Query
```

The initial cost may be worthwhile if the graph receives many future updates and queries.

---

# Amortized Update Time

### Q16: What does amortized update time mean?
Ans: Instead of requiring every single update to have the same cost, we measure the average cost across a sequence of updates.

Suppose five updates cost:

```
1
1
1
1
20
```

Total:

```
24
```

Average:

```
24 / 5 = 4.8
```

One update was expensive, but the average across the sequence was much smaller.

Dynamic algorithm analysis frequently uses amortized complexity.

---

# Dynamic vs Repeated Static Computation

Suppose a graph receives:

```
1000 updates
```

Approach A:

```
For every update:
    Run Dijkstra from scratch
```

Approach B:

```
Maintain shortest-path information
Update only affected information
```

Which is faster?

The answer depends on:

- graph size
- graph density
- number of updates
- type of updates
- how many vertices are affected
- number of shortest-path queries
- overhead of the dynamic method

This is an excellent experimental question.

---

# Dynamic Shortest Paths vs Dijkstra

### Dijkstra

Assumes:

```
Graph remains fixed during computation
```

Input:

```
Graph + Source
```

Output:

```
Shortest distances
```

If graph changes:

```
Run again
```

unless another maintenance method is used.

---

### Dynamic Shortest Paths

Assumes:

```
Graph may repeatedly change
```

Goal:

```
Reuse existing information
```

and update shortest paths efficiently.

---

# Dynamic Shortest Paths vs Bellman-Ford

Bellman-Ford repeatedly relaxes edges in a static graph computation.

Dynamic shortest-path maintenance responds to:

```
changes in the graph itself
```

These are different concepts.

Bellman-Ford:

```
Graph fixed
Negative edges allowed
Repeated relaxation
```

Dynamic shortest paths:

```
Graph changes over time
Maintain shortest-path information
```

---

# Dynamic Shortest Paths vs Dynamic Programming

### Q17: Does "dynamic" mean Dynamic Programming?
Ans: No.

The word:

```
dynamic
```

here means:

```
the graph changes over time
```

It does not mean that Dynamic Shortest Paths is simply Dynamic Programming.

The terms refer to different ideas.

---

# Robotics Connection

Dynamic shortest paths are particularly relevant to robotics.

Imagine a robot plans:

```
Robot -> Hallway -> Door -> Goal
```

Then a new obstacle appears:

```
Door blocked
```

The robot's previous route is no longer valid.

Instead of rebuilding every piece of planning information from scratch, replanning algorithms can attempt to reuse previous search results.

Algorithms such as:

```
Lifelong Planning A*
D* Lite
```

are related to this idea and are important in robotics and changing environments.

They are more advanced topics and do not need to be added to our core notes right now.

---

# Navigation Example

Suppose a navigation system calculated:

```
Atlanta -> Road A -> Road B -> Destination
```

Then traffic causes:

```
Road B travel time:
5 minutes -> 30 minutes
```

The graph's edge weight changed.

The navigation system may need to find a better route.

This is a real-world example of shortest-path computation in a changing weighted graph.

---

# Network Example

Suppose routers form:

```
A -> B -> C -> D
```

and link:

```
B -> C
```

fails.

Routes that depended on that connection must change.

Dynamic graph concepts therefore also appear naturally in network routing.

---

# When Is Recomputing From Scratch Actually Better?

### Q18: Should we always use a dynamic algorithm when the graph changes?
Ans: No.

Suppose:

```
Graph is small
```

and updates happen rarely.

Running:

```
Dijkstra again
```

may be simpler and fast enough.

A complicated dynamic method may have:

```
Preprocessing cost
Memory overhead
Maintenance overhead
Implementation complexity
```

So the real question is:

> Under what conditions does maintaining shortest paths become better than recomputing them?

That is a much more interesting question than assuming dynamic algorithms are always superior.

---

# Important Tradeoffs

Dynamic shortest-path methods may trade between:

```
Preprocessing time
Update time
Query time
Memory
Accuracy
Implementation complexity
```

Improving one may make another worse.

For example:

```
More stored information
        ->
Potentially faster updates
        ->
Higher memory usage
```

or:

```
Approximate distances
        ->
Potentially faster maintenance
        ->
Less exact answers
```

---

# Complexity

### Q19: What is the complexity of Dynamic Shortest Paths?
Ans: There is no single complexity.

Because Dynamic Shortest Paths is a family of problems and algorithms, complexity depends on the specific method.

Common measures include:

```
Preprocessing Time

Update Time

Query Time

Space Complexity
```

For comparison, rerunning heap-based Dijkstra after every update would cost approximately:

```
O((V + E) log V)
```

per recomputation under a common adjacency-list implementation.

A dynamic method attempts to improve on repeated full recomputation under the conditions for which it was designed.

---

# Comparison

- BFS
  - Graph changes? no during computation
  - Main goal: unweighted shortest paths

- Dijkstra
  - Graph changes? no during computation
  - Main goal: non-negative weighted shortest paths

- Bellman-Ford
  - Graph changes? no during computation
  - Main goal: negative-weight shortest paths

- A*
  - Graph changes? no during computation
  - Main goal: goal-directed shortest path

- Dynamic Shortest Paths
  - Graph changes? yes
  - Main goal: maintain paths as graph changes

---

# When Should I Think About Dynamic Shortest Paths?

Ask:

```
Does my graph change over time?
        |
       Yes
        |
Do I repeatedly need shortest paths?
        |
       Yes
        |
Would recomputing from scratch
be expensive?
        |
       Yes
        |
Dynamic shortest-path techniques
may be useful
```

---

# Key Things to Remember

### Rule 1

Dynamic Shortest Paths means:

```
maintaining shortest paths
while the graph changes
```

---

### Rule 2

It is:

```
NOT one algorithm
```

It is a family of problems and techniques.

---

### Rule 3

Three major categories:

```
Incremental
Decremental
Fully Dynamic
```

---

### Rule 4

Important graph changes include:

```
Edge insertion
Edge deletion
Weight decrease
Weight increase
```

---

### Rule 5

Not every graph update affects existing shortest paths.

---

### Rule 6

A local update can sometimes produce:

```
local effect
```

but can also produce:

```
global effect
```

---

### Rule 7

Dynamic algorithms try to:

```
reuse previous information
```

rather than automatically:

```
recompute everything
```

---

### Rule 8

Important performance measurements include:

```
Preprocessing time
Update time
Query time
Memory
```

---

### Rule 9

Dynamic does NOT mean:

```
Dynamic Programming
```

It means:

```
Graph changes over time
```

---

### Rule 10

Sometimes:

```
Recompute from scratch
```

is still the best practical solution.

---

# Questions to Test My Understanding

Before considering Dynamic Shortest Paths complete, I should be able to answer:

## Conceptual

1. What does Dynamic Shortest Paths mean?
2. Why is it not one specific algorithm?
3. What is the difference between static and dynamic shortest paths?
4. What is an incremental problem?
5. What is a decremental problem?
6. What is a fully dynamic problem?
7. What happens when an edge is inserted?
8. What happens when an edge is deleted?
9. What happens when an edge weight decreases?
10. What happens when an edge weight increases?
11. Why does not every graph update necessarily change shortest paths?
12. What information could be reused from the previous shortest-path computation?
13. What is a shortest-path tree?
14. Why can a small graph change have a global effect?
15. Why can deletions be harder to repair than insertions?
16. What is update time?
17. What is query time?
18. What is preprocessing time?
19. What is amortized update time?
20. What is the difference between exact and approximate dynamic shortest paths?
21. Why might recomputing Dijkstra sometimes be better than maintaining a dynamic structure?
22. Does dynamic mean Dynamic Programming?
23. How are dynamic shortest paths relevant to robotics?
24. What are Lifelong Planning A* and D* Lite generally designed to help with?

---

# Questions Worth Investigating During Experiments

This topic gives us several excellent later extensions to the main experiments.

## 1. Full Recalculation vs Local Update

Generate a graph.

Run Dijkstra.

Then change:

```
one edge
```

Compare:

```
Run Dijkstra from scratch

vs

Repair only affected distances
```

Measure:

```
runtime
nodes processed
edges examined
memory
```

---

## 2. Edge Insertion

Start with a graph.

Then repeatedly add edges.

Ask:

```
How often does a new edge actually change
the shortest path?
```

---

## 3. Edge Deletion

Delete:

```
random edges
```

and compare them with deleting:

```
edges belonging to the current shortest-path tree
```

Hypothesis:

Tree-edge deletions should be more likely to affect shortest paths.

But we should test rather than assume.

---

## 4. Weight Increase

Take an edge currently used by a shortest path.

Increase its cost by:

```
10%
50%
100%
500%
```

Ask:

```
At what point does an alternative route become better?
```

---

## 5. Weight Decrease

Choose an unused edge and gradually reduce its weight.

Ask:

```
When does the edge become part of the shortest path?
```

---

## 6. Graph Density

Compare:

```
sparse graphs
vs
dense graphs
```

Do dense graphs provide more alternative routes when an edge is removed?

Does that make shortest paths more stable or make update processing more expensive?

---

## 7. Update Location

Compare changes:

```
near the source

near the target

on the current shortest path

far away from the current shortest path
```

How does update location affect the amount of recomputation required?

---

## 8. Number of Updates

Test:

```
1 update
10 updates
100 updates
1000 updates
```

At what point does maintaining information become more attractive than repeatedly recomputing from scratch?

---

## 9. Dynamic A* / Robotics Extension

Later, after the main research is complete, create a changing grid:

```
Robot -> Goal
```

Introduce obstacles while the robot moves.

Compare:

```
Re-run A*

vs

a replanning method such as D* Lite
```

This would be a natural future robotics extension rather than something required for our first experiment set.

---

# Final Mental Model

Static shortest paths are like receiving a printed road map.

You calculate:

```
Home -> A -> B -> C -> Destination
```

and assume the roads stay the same.

Dynamic shortest paths are like using live navigation.

You calculate:

```
Home -> A -> B -> C -> Destination
```

Then suddenly:

```
ROAD C CLOSED
```

or:

```
ROAD B TRAFFIC
5 min -> 40 min
```

or:

```
NEW ROAD OPENED
```

Now the question is not simply:

```
What is the shortest path?
```

It becomes:

```
I ALREADY calculated the shortest path.

The graph just changed.

How much of my previous work can I reuse?
```

That is the heart of Dynamic Shortest Paths.

> Do not automatically throw away everything you already know just because part of the graph changed.
