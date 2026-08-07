## Research Notes

### Questions Explored

- Why doesn't DFS guarantee the shortest path?
- Why does DFS use a stack (or recursion) instead of a queue?
- What happens if the visited set is removed?
- How does recursive DFS differ from iterative DFS?
- Why does DFS backtrack?
- What is actually happening in the recursion stack during DFS?
- How does DFS behave on graphs containing cycles?
- Why is DFS commonly used for topological sorting?
- How does DFS detect cycles?
- When is DFS a better choice than BFS?
- What are the memory advantages and disadvantages of DFS compared to BFS?
- How does graph structure (sparse vs. dense) affect DFS performance?
- Can DFS be modified to find the shortest path?
- Why is DFS useful for maze-solving and backtracking problems?
- How would DFS change if the graph were directed instead of undirected?
- How does DFS work on disconnected graphs?




Answers:

## Q1: Why doesn't DFS guarantee the shortest path? (IMP)

**Answer:**

DFS explores one path as deeply as possible before considering other paths. It returns the first path it finds, which may not be the shortest. Because it does not compare all possible paths before making decisions, DFS cannot guarantee the shortest path.

---

## Q2: Why does DFS use a stack (or recursion) instead of a queue? (IMP)

**Answer:**

DFS uses a **stack**, either explicitly or through recursion, because it follows the **Last-In, First-Out (LIFO)** principle. This allows the algorithm to continue exploring the most recently discovered vertex until it reaches a dead end. Once no further progress can be made, the stack naturally allows DFS to backtrack to the previous vertex and explore another path.

---

## Q3: What happens if the visited set is removed? (IMP)

**Answer:**

Without a visited set, DFS may repeatedly visit the same vertices. In graphs containing cycles, this can cause infinite recursion (or an infinite loop in the iterative version), preventing the algorithm from terminating correctly.

---

## Q4: How does recursive DFS differ from iterative DFS? (IMP)

**Answer:**

Both versions perform the same traversal but manage the stack differently.

- **Recursive DFS** uses the program's built-in call stack.
- **Iterative DFS** uses a stack data structure created by the programmer.

Both explore vertices in depth-first order and have the same time complexity.

---

## Q5: Why does DFS backtrack? (IMP)

**Answer:**

DFS backtracks because it explores one path until it can no longer continue. When it reaches a dead end or a vertex with no unvisited neighbors, it returns to the previous vertex to explore any remaining unexplored paths. This process continues until every reachable vertex has been visited.

---

## Q6: What is actually happening in the recursion stack during DFS? (IMP)

**Answer:**

Every recursive call is placed onto the program's call stack. When DFS visits a new vertex, the current function pauses while a new function call begins for the next vertex. Once a path has been completely explored, each function returns in reverse order, allowing DFS to continue exploring any remaining neighbors.

Example:

```
dfs(A)
 ↓
dfs(B)
 ↓
dfs(C)
 ↓
dfs(D)

D finishes
↑
Return to C
↑
Return to B
↑
Return to A
```

The recursion stack remembers **where the algorithm needs to return after finishing the current path**.

---

## Q7: How does DFS behave on graphs containing cycles? (IMP)

**Answer:**

DFS works correctly on graphs containing cycles as long as a **visited set** is used. Once a vertex has been visited, it is not explored again. Without a visited set, DFS may repeatedly traverse the same cycle and never terminate.

---

## Q8: Why is DFS commonly used for topological sorting? (IMP)

**Answer:**

DFS naturally explores all dependencies before finishing a vertex. A vertex is added to the output only after all of its neighbors have been fully explored. This produces an ordering where every dependency appears before the tasks that depend on it, making DFS well suited for Topological Sort.

---

## Q9: How does DFS detect cycles? (IMP)

**Answer:**

The method depends on the type of graph.

- In **undirected graphs**, DFS detects a cycle if it reaches a previously visited vertex that is **not the current vertex's parent**.
- In **directed graphs**, DFS keeps track of both visited vertices and the current recursion stack. If DFS reaches a vertex that is already in the recursion stack, a cycle has been found.

---

## Q10: When is DFS a better choice than BFS? (IMP)

**Answer:**

DFS is preferred when exploring deep paths or when the shortest path is not required. It is commonly used for:

- Topological Sorting
- Cycle Detection
- Maze Solving
- Backtracking Problems
- Finding Connected Components

DFS is also useful when memory is limited because it often stores fewer vertices than BFS.

---

## Q11: What are the memory advantages and disadvantages of DFS compared to BFS? (IMP)

**Answer:**

DFS generally uses less memory because it stores only the current path being explored. BFS stores an entire level of the graph in its queue, which can require much more memory on wide graphs.

However, recursive DFS may cause a **stack overflow** if the graph is extremely deep.

---

## Q12: How does graph structure (sparse vs. dense) affect DFS performance? (IMP)

**Answer:**

DFS has a time complexity of **O(V + E)** regardless of graph structure.

In **sparse graphs**, there are relatively few edges, so DFS performs fewer neighbor checks.

In **dense graphs**, there are many more edges to examine, so DFS performs more work even though the overall complexity remains **O(V + E)**.

---

## Q13: Can DFS be modified to find the shortest path? (IMP)

**Answer:**

DFS can be modified to find the shortest path by exploring **every possible path** and keeping track of the shortest one found. However, this is highly inefficient because the number of possible paths can grow exponentially. For shortest-path problems, BFS (for unweighted graphs) or Dijkstra's Algorithm (for weighted graphs) are much better choices.

---

## Q14: Why is DFS useful for maze-solving and backtracking problems? (IMP)

**Answer:**

DFS naturally follows one path until it reaches a dead end. If the path does not lead to a solution, the algorithm backtracks and tries another path. This behavior makes DFS ideal for maze-solving, puzzle solving, backtracking algorithms, and searching through decision trees.

---

## Q15: How would DFS change if the graph were directed instead of undirected? (IMP)

**Answer:**

The traversal process remains the same, but DFS follows the direction of each edge. If there is an edge from A to B, DFS can travel from A to B, but not necessarily from B to A. Directed graphs also require different techniques for cycle detection and are commonly used with algorithms such as Topological Sort.

## Q16: How does DFS traverse a disconnected graph?

A standard DFS only explores the connected component containing the starting vertex. Once every reachable vertex has been visited and the recursion finishes (or the stack becomes empty), the algorithm terminates. Any vertices belonging to other disconnected components remain unvisited because there is no path leading to them. To traverse the entire graph, we use an outer loop that checks every vertex. If a vertex has not yet been visited, we start a new DFS from that vertex. Since every visited vertex is stored in the `visited` set, previously explored components are skipped automatically.

For example, consider the graph below:

Component 1:

A --- B --- C


Component 2:

D --- E


If DFS starts from **A**, it will visit:


A → B → C


Vertices D and E remain unvisited because they are not connected to A. The outer loop eventually reaches D, notices that it has not been visited, and starts another DFS. The final traversal becomes:

```text
A → B → C → D → E
```

### Python Example

```python
def dfs(graph, node, visited):
    if node in visited:
        return

    visited.add(node)
    print(node)

    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)


graph = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["E"],
    "E": ["D"]
}

visited = set()

# This section below checks for disconnected components
for node in graph:
    if node not in visited:
        dfs(graph, node, visited)
```

This approach ensures that every connected component is explored exactly once. Although DFS may be started multiple times, each vertex is still visited only once, so the overall time complexity remains **O(V + E)**.