# Branch and Bound

## Overview

### Q1: What is Branch and Bound?
Ans: Branch and Bound is a general optimization and search strategy used to find an optimal solution among many possible solutions.

Unlike BFS, Dijkstra, or Bellman-Ford, Branch and Bound is not one single fixed algorithm.

It is a framework based on three main ideas:

```
BRANCH -> create possible choices

BOUND -> estimate how good a branch could possibly become

PRUNE -> stop exploring branches that cannot beat the best solution
```

The goal is to avoid exploring parts of the search space that cannot possibly contain a better solution.

---

### Q2: What kind of problems is Branch and Bound used for?
Ans: Branch and Bound is commonly used for optimization problems where there may be a huge number of possible solutions.

Examples include:

- Traveling Salesman Problem
- Knapsack Problem
- Scheduling
- Assignment problems
- Integer programming
- Routing problems
- Combinatorial optimization

The important question is usually:

> Out of all possible solutions, which one has the minimum or maximum cost?

---

## Intuition

Imagine we are trying to find the cheapest route.

Suppose we already found a complete solution costing:

```
20
```

Now we begin exploring another branch.

After examining part of that branch, we determine:

```
Best possible outcome from this branch >= 25
```

But we already have:

```
Best known solution = 20
```

There is no reason to continue exploring that branch.

Even under the most optimistic scenario, it cannot beat 20.

So we:

```
PRUNE
```

the branch.

---

## Simple Mental Example

Suppose our search tree looks like:

```
                    START
                   /     \
                  A       B
                /   \    / \
               C     D  E   F
```

Assume we are minimizing cost.

Suppose exploring the left side gives us a complete solution:

```
Best known cost = 15
```

Now consider branch B.

Suppose its bound tells us:

```
Best possible solution through B >= 22
```

Since:

```
22 > 15
```

branch B cannot possibly improve our current solution.

Therefore:

```
                    START
                   /     \
                  A       B  X
                /   \
               C     D
```

We never need to explore:

```
E
F
```

That is the power of pruning.

---

# The Three Core Ideas

## 1. Branch

### Q3: What does "branch" mean?
Ans: Branching means dividing the problem into smaller choices or possibilities.

For example, in a route problem:

```
Current City = A
```

Possible next choices:

```
A -> B

A -> C

A -> D
```

Each choice creates a new branch in the search tree.

---

## 2. Bound

### Q4: What is a bound?
Ans: A bound is an estimate of the best possible result that could still come from a branch.

If we are minimizing:

```
bound = optimistic minimum possible cost
```

If that optimistic minimum is already worse than our current best complete solution, the branch is useless.

Example:

```
Current best solution = 30

Branch X lower bound = 40
```

Even under the best possible outcome:

```
Branch X >= 40
```

Therefore:

```
40 > 30
```

and we can prune Branch X.

---

## 3. Prune

### Q5: What does pruning mean?
Ans: Pruning means intentionally not exploring a branch because we can prove that it cannot produce a better solution than the best one already found.

Conceptually:

```
Can this branch beat our best solution?
            |
         /     \
       Yes      No
        |        |
     Explore    PRUNE
```

Pruning is what can make Branch and Bound dramatically more efficient than exhaustive search.

---

# Incumbent

### Q6: What is the incumbent?
Ans: The incumbent is the best complete solution found so far.

For a minimization problem:

```
incumbent = smallest complete cost found so far
```

Example:

```
First solution found = 50

incumbent = 50
```

Later:

```
New solution = 37

incumbent = 37
```

Later:

```
New solution = 42
```

We keep:

```
incumbent = 37
```

The incumbent gives us something against which bounds can be compared.

---

# Lower and Upper Bounds

### Q7: What is the difference between lower and upper bounds?
Ans: It depends on whether we are minimizing or maximizing.

For a minimization problem, a lower bound estimates:

```
The cheapest this branch could possibly become.
```

If:

```
lower_bound >= incumbent
```

we can prune.

For example:

```
incumbent = 20

lower_bound = 25
```

Then:

```
25 >= 20
```

so the branch cannot improve the best solution.

---

For a maximization problem, we often use an upper bound representing:

```
The largest value this branch could possibly achieve.
```

If that upper bound cannot beat the current best solution, we prune.

---

# Why the Bound Must Be Safe

### Q8: Why can't we just guess the bound?
Ans: Because pruning removes an entire section of the search space.

If the bound is wrong, we might accidentally prune the branch containing the true optimal solution.

Suppose:

```
Actual best possible cost through branch = 10
```

but our incorrect bound says:

```
bound = 25
```

and our incumbent is:

```
20
```

We would prune:

```
25 >= 20
```

even though that branch actually contained a solution costing:

```
10
```

We would lose the optimal answer.

Therefore the bound must be mathematically valid.

---

# Tight vs Loose Bounds

### Q9: What makes a good bound?
Ans: A good bound should be:

```
SAFE
```

and preferably:

```
TIGHT
```

A loose bound may be correct but not very useful.

Example:

```
True best possible = 20

Bound = 0
```

Technically the branch cannot do better than 0, so the bound may be safe in some minimization formulation.

But it tells us very little.

A tighter bound might be:

```
Bound = 18
```

which is much closer to the true possible result.

Tighter bounds usually allow more pruning.

However, complicated bounds may also take more time to calculate.

This creates an important tradeoff:

```
Better bound
    ->
More pruning
    ->
But possibly more computation per node
```

---

# Search Tree

Branch and Bound usually operates over a state-space tree.

The root represents:

```
No decisions made yet
```

Each branch represents:

```
One additional decision
```

Leaves often represent:

```
Complete solutions
```

Example:

```
                     START
                   /   |   \
                  A    B    C
                 / \       / \
                D   E     F   G
```

Branch and Bound explores this tree while using bounds to avoid exploring unnecessary sections.

---

# Branch and Bound vs Brute Force

### Q10: How is Branch and Bound different from brute force?

Brute force:

```
Generate every possible solution
        |
        v
Evaluate all of them
        |
        v
Choose the best
```

Branch and Bound:

```
Explore possibilities
        |
        v
Use bounds
        |
        v
Eliminate impossible-to-improve branches
        |
        v
Explore only promising regions
```

In the worst case, Branch and Bound may still need to explore a huge portion of the search space.

But good bounds can reduce the practical search dramatically.

---

# Example: Traveling Salesman Problem

Suppose we have cities:

```
A
B
C
D
```

We want:

```
Start at A
Visit every city
Return to A
Minimize total cost
```

Possible route:

```
A -> B -> C -> D -> A
```

Another:

```
A -> C -> B -> D -> A
```

Another:

```
A -> D -> C -> B -> A
```

The number of possible tours grows extremely quickly as the number of cities increases.

Branch and Bound can explore partial tours while estimating:

```
What is the minimum possible total cost if I continue from here?
```

If that estimate is already worse than our best known complete tour:

```
PRUNE
```

---

# Simplified Route Example

Suppose:

```
Best complete route found = 25
```

We are currently exploring:

```
A -> C -> D
```

Current cost:

```
18
```

Suppose we know completing the remaining route must cost at least:

```
10
```

Then our lower bound is:

```
18 + 10 = 28
```

Since:

```
28 > 25
```

this branch cannot beat the incumbent.

Therefore:

```
A -> C -> D -> ...
```

is pruned.

---

# Generic Algorithm Steps

For a minimization problem:

1. Create the initial/root state.
2. Set the best known solution to infinity.
3. Put the root into a collection of live states.
4. Select a state to explore.
5. If it represents a complete solution:
   - Compare it with the incumbent.
   - Update the incumbent if better.
6. Otherwise:
   - Branch into possible child states.
7. Calculate a lower bound for each child.
8. If:

```
bound < incumbent
```

keep the child.

9. Otherwise:

```
PRUNE
```

10. Continue until no live states remain.
11. Return the incumbent.

---

# Generic Python Structure

Branch and Bound does not have one universal implementation because the branching and bounding logic depends on the optimization problem.

A simplified framework looks like:

```python
def branch_and_bound(initial_state):

    best_solution = None
    best_cost = float("inf")

    states = [initial_state]

    while states:

        state = states.pop()

        # If this is a complete solution
        if is_complete(state):

            cost = solution_cost(state)

            if cost < best_cost:
                best_cost = cost
                best_solution = state

            continue

        # Create possible next decisions
        for child in branch(state):

            lower_bound = calculate_bound(child)

            # Only explore if the child can still improve
            if lower_bound < best_cost:
                states.append(child)

    return best_solution, best_cost
```

The important pieces are:

```
branch()
calculate_bound()
is_complete()
solution_cost()
```

Their implementation depends entirely on the problem being solved.

---

# Code Walkthrough

## 1. Best Known Solution

```
best_cost = float("inf")
```

Initially, we have no solution.

For minimization:

```
best known cost = infinity
```

---

## 2. Select a State

```
state = states.pop()
```

This example uses stack-like behavior.

But Branch and Bound can use different strategies for selecting which state to explore next.

---

## 3. Check for Complete Solution

```
if is_complete(state):
```

If the state represents a complete solution, calculate its actual cost.

---

## 4. Update the Incumbent

```python
if cost < best_cost:
    best_cost = cost
    best_solution = state
```

We found a better complete solution.

---

## 5. Branch

```python
for child in branch(state):
```

Generate possible next decisions.

---

## 6. Calculate Bound

```python
lower_bound = calculate_bound(child)
```

Estimate the best possible solution reachable through this child.

---

## 7. Prune

```python
if lower_bound < best_cost:
    states.append(child)
```

If the child can still potentially beat our incumbent, keep exploring it.

Otherwise, it disappears from consideration.

---

# Search Strategies

### Q11: In what order can Branch and Bound explore states?
Ans: Several strategies are possible.

## Depth-First Branch and Bound

Use a stack:

```
LIFO
```

Behavior resembles:

```
DFS
```

Advantage:

A complete solution may be found quickly, giving us an incumbent early.

Memory can also be relatively low.

---

## Breadth-First Branch and Bound

Use a queue:

```
FIFO
```

Behavior resembles:

```
BFS
```

Explores states level by level.

This can require substantial memory.

---

## Best-First Branch and Bound

Use a priority queue.

Select the state with the most promising bound.

Example:

```
Branch A bound = 15
Branch B bound = 7
Branch C bound = 21
```

For minimization, explore:

```
Branch B
```

first.

This resembles ideas we have already seen with:

```
Dijkstra
A*
```

because promising states receive priority.

---

# Branch and Bound vs BFS

### BFS

Goal:

```
Explore graph level by level
```

Uses:

```
Queue
```

Often used for:

```
unweighted shortest paths
```

---

### Branch and Bound

Goal:

```
Find an optimal solution while pruning impossible-to-improve choices
```

May use:

```
stack
queue
priority queue
```

The central feature is not the data structure.

It is:

```
BOUNDING + PRUNING
```

---

# Branch and Bound vs Dijkstra

### Q12: Is Dijkstra a Branch and Bound algorithm?
Ans: They share some ideas, such as prioritizing promising states, but Dijkstra is a specific shortest-path algorithm with its own correctness properties.

Branch and Bound is a broader optimization framework.

Dijkstra:

```
specific graph shortest-path algorithm
```

Branch and Bound:

```
general optimization search framework
```

It is better to treat them as related ideas rather than calling them the same algorithm.

---

# Branch and Bound vs A*

### Q13: How is Branch and Bound related to A*?
Ans: Both use information about future possibilities to avoid unnecessary exploration.

A* uses:

```
f(n) = g(n) + h(n)
```

where:

```
g(n) = cost already traveled

h(n) = estimated remaining cost
```

Branch and Bound similarly asks:

```
What is the best possible solution that could come from this branch?
```

If the branch cannot beat the incumbent:

```
PRUNE
```

The concepts are related, but A* is a specific pathfinding algorithm while Branch and Bound is a broader optimization framework.

---

# Branch and Bound vs Backtracking

### Q14: What is the difference between Branch and Bound and Backtracking?
Ans: Both explore a state-space tree and abandon branches.

But the reason for abandoning them differs.

Backtracking usually prunes because:

```
This partial solution violates a constraint.
```

Example:

```
Two queens attack each other
-> stop exploring
```

Branch and Bound usually prunes because:

```
This branch cannot produce a solution better than our incumbent.
```

So:

```
Backtracking
-> feasibility-based pruning

Branch and Bound
-> optimization-based pruning
```

The techniques can overlap in real algorithms.

---

# Optimization Direction Matters

## Minimization

We want:

```
smallest value
```

Maintain:

```
best known upper bound from a complete solution
```

Use branch lower bounds.

Prune when:

```
lower_bound >= best_cost
```

---

## Maximization

We want:

```
largest value
```

Maintain the best known complete value.

Use branch upper bounds.

Prune when:

```
upper_bound <= best_value
```

The direction of the inequality changes depending on the optimization objective.

---

# Correctness

### Q15: How can Branch and Bound still guarantee an optimal solution if it skips branches?
Ans: Because it only prunes branches that are provably incapable of beating the incumbent.

Suppose:

```
incumbent = 20
```

and a valid lower bound proves:

```
Every solution in Branch X costs at least 30.
```

Then Branch X cannot contain the optimum if we already have a solution costing 20.

Skipping it cannot remove a better solution.

Correctness therefore depends heavily on:

```
VALID BOUNDS
```

---

# Does Branch and Bound Always Make Search Fast?

### Q16: Is Branch and Bound always efficient?
Ans: No.

In the worst case, the bounds may fail to eliminate many branches.

Then Branch and Bound may behave similarly to exhaustive search.

For many combinatorial optimization problems, worst-case runtime can still be:

```
exponential
```

The practical performance depends heavily on:

- quality of bounds
- branching strategy
- search order
- how quickly a strong incumbent is found
- structure of the problem

---

# Why Finding a Good Solution Early Matters

### Q17: Why does the incumbent matter so much?
Suppose initially:

```
best_cost = infinity
```

Almost every branch looks potentially useful because:

```
bound < infinity
```

Now suppose we quickly find:

```
best_cost = 100
```

Some branches can be pruned.

Later we find:

```
best_cost = 50
```

Even more branches can be pruned.

Then:

```
best_cost = 30
```

More pruning becomes possible.

Therefore:

> A strong incumbent found early can dramatically reduce the remaining search.

This means search order can have a major impact on practical performance.

---

# Bound Quality Tradeoff

Suppose we have two bounding methods.

### Bound A

Takes:

```
1 microsecond
```

but is loose.

### Bound B

Takes:

```
1 millisecond
```

but is much tighter.

Bound B might prune far more branches.

But calculating it is also more expensive.

So the fastest algorithm is not necessarily the one with the mathematically strongest bound.

There is a tradeoff between:

```
BOUND COMPUTATION COST
```

and:

```
SEARCH SPACE REDUCTION
```

This is an excellent experimental question.

---

# Practical Use Cases

Branch and Bound appears in problems such as:

### Traveling Salesman

```
Find minimum-cost tour.
```

### Knapsack

```
Choose items that maximize value while respecting capacity.
```

### Scheduling

```
Assign jobs to minimize completion time or cost.
```

### Assignment Problems

```
Assign workers to tasks optimally.
```

### Integer Optimization

```
Find the best solution where variables must take discrete/integer values.
```

---

# Complexity

### Q18: What is the time complexity of Branch and Bound?
Ans: There is no single universal complexity because Branch and Bound is a framework rather than one fixed algorithm.

For many problems, worst-case behavior remains:

```
exponential
```

because the algorithm may need to explore most or all of the search tree.

The entire point of Branch and Bound is to make the practical search space much smaller through pruning.

---

### Q19: What is the space complexity?
Ans: This depends on the search strategy.

Depth-first implementations may require substantially less memory than breadth-first or best-first implementations.

A best-first implementation may maintain many live states in a priority queue.

Therefore space depends on:

```
problem
search tree
search strategy
number of live branches
```

---

# Comparison

- Brute Force
  - Main idea: explore everything
  - Pruning reason: none

- BFS
  - Main idea: explore level by level
  - Pruning reason: usually visited states

- DFS
  - Main idea: explore deeply
  - Pruning reason: usually visited states

- Backtracking
  - Main idea: explore choices
  - Pruning reason: constraint violation

- Branch and Bound
  - Main idea: explore optimization choices
  - Pruning reason: cannot beat incumbent

- A*
  - Main idea: prioritize promising paths
  - Pruning reason: cost + heuristic reasoning

---

# When Should I Think About Branch and Bound?

Ask:

```
Do I have an optimization problem?
        |
       Yes
        |
Are there many possible solutions?
        |
       Yes
        |
Can I calculate a valid bound
on partial solutions?
        |
       Yes
        |
Branch and Bound may be useful
```

---

# Key Things to Remember

### Rule 1

Branch and Bound is a:

```
general optimization framework
```

not one single fixed graph algorithm.

---

### Rule 2

The three central ideas are:

```
BRANCH
BOUND
PRUNE
```

---

### Rule 3

The best complete solution found so far is called the:

```
INCUMBENT
```

---

### Rule 4

For minimization:

```
lower_bound >= best_cost
        ->
      PRUNE
```

---

### Rule 5

For maximization:

```
upper_bound <= best_value
        ->
      PRUNE
```

---

### Rule 6

Bounds must be:

```
VALID
```

Otherwise we may prune the true optimal solution.

---

### Rule 7

Tighter bounds generally mean:

```
more pruning
```

but may require:

```
more computation
```

---

### Rule 8

Finding a strong incumbent early can dramatically improve pruning.

---

### Rule 9

Branch and Bound can still have:

```
exponential worst-case runtime
```

It does not magically make hard optimization problems easy.

---

# Questions to Test My Understanding

Before considering Branch and Bound complete, I should be able to answer:

## Conceptual

1. What is Branch and Bound?
2. Why is it considered a framework rather than one specific algorithm?
3. What does branching mean?
4. What is a bound?
5. What does pruning mean?
6. What is an incumbent?
7. Why is the incumbent important?
8. For minimization, when can a branch be pruned?
9. For maximization, when can a branch be pruned?
10. Why must a bound be valid?
11. What is the difference between a tight and loose bound?
12. Why isn't the tightest possible bound automatically the fastest approach?
13. How is Branch and Bound different from brute force?
14. How is Branch and Bound different from backtracking?
15. How is Branch and Bound related to A*?
16. Can Branch and Bound use DFS?
17. Can Branch and Bound use BFS?
18. Can Branch and Bound use a priority queue?
19. Why does finding a good solution early matter?
20. Does Branch and Bound guarantee polynomial runtime?
21. Why can it still be exponential?
22. What guarantees that pruning does not remove the optimal solution?

---

# Questions Worth Investigating During Experiments

Branch and Bound is somewhat different from our shortest-path algorithms, so it may eventually deserve a separate experimental category.

## 1. Branch and Bound vs Brute Force

For the same optimization problem:

```
How many states does brute force explore?

How many states does Branch and Bound explore?
```

---

## 2. Pruning Rate

Measure:

```
branches generated

branches explored

branches pruned
```

Then calculate:

```
pruning rate
```

How does pruning change as the problem grows?

---

## 3. Bound Quality

Compare:

```
simple loose bound

vs

expensive tight bound
```

Measure:

```
runtime
states explored
states pruned
bound calculation time
```

Does stronger pruning compensate for the extra computation?

---

## 4. Search Strategy

Compare:

```
Depth-First Branch and Bound

Breadth-First Branch and Bound

Best-First Branch and Bound
```

Measure:

```
runtime
memory
states explored
time until first complete solution
time until optimal solution
```

---

## 5. Incumbent Quality

Try giving the algorithm:

```
no initial solution

random initial solution

good heuristic solution
```

Does starting with a strong incumbent increase pruning?

---

## 6. Problem Size

As the number of decisions increases:

```
How quickly does the search space grow?
```

And:

```
How much of that search space does Branch and Bound actually avoid?
```

---

## 7. Worst-Case Behavior

Can we construct problem instances where:

```
almost nothing gets pruned?
```

If so, Branch and Bound should begin behaving much more like exhaustive search.

This would demonstrate the difference between:

```
worst-case complexity
```

and:

```
practical performance
```

---

# Final Mental Model

Imagine exploring a gigantic dungeon looking for the cheapest possible treasure route.

Brute force says:

```
Search every corridor.
```

Branch and Bound says:

```
Search a corridor.

Estimate the BEST result
that corridor could possibly give.

Can it beat our current treasure route?
        |
      /   \
    Yes    No
     |      |
 Explore   Seal the corridor forever
```

That sealed corridor is:

```
PRUNED
```

The entire strategy can therefore be remembered as:

```
BRANCH
   |
   v
BOUND
   |
   v
Can it beat the incumbent?
   |
 /   \
Yes   No
 |     |
Explore PRUNE
```

The core idea is:

> Do not waste time exploring a branch once you can prove that it cannot beat the best solution already found.
