# BFS Research Notes

Questions I came across while studying:

Q: Why doesn't BFS work with weighted edges?
Q: Could BFS be modified to support weighted graphs?
Q: What if all edge weights are either 0 or 1?
Q: Which graph structures maximize BFS memory usage?
Q: How does queue order affect traversal?
Q: How does graph density influence performance?
Q: What metrics should be measured when benchmarking BFS against DFS, Dijkstra, and A*?
Q: Why does BFS use a queue?
Q: Why can't BFS solve weighted shortest path problems?
Q: What happens if we remove the visited set?
Q: What is the difference between BFS and DFS?
Q: What is the time complexity?
Q: Can BFS detect cycles?
Q: Why does BFS guarantee the shortest path?
Q: How does BFS work on disconnected graphs?







Answers:

## Q1: Why doesn't BFS work with weighted edges? (IMP)

**Answer:**

BFS assumes that every edge has the same cost. It explores the graph level by level, meaning it minimizes the **number of edges** rather than the **total path cost**. When edge weights differ, a path with fewer edges may actually be more expensive than a path with more edges. Since BFS ignores edge weights, it cannot guarantee the minimum-cost path.

---

## Q2: Could BFS be modified to support weighted graphs? (IMP)

**Answer:**

Standard BFS cannot solve arbitrary weighted shortest-path problems because it is designed for equal-weight edges. However, if all edge weights are either **0 or 1**, a modified version called **0-1 BFS** can be used. For general weighted graphs with non-negative weights, Dijkstra's Algorithm is the correct choice.

---

## Q3: What if all edge weights are either 0 or 1? (IMP)

**Answer:**

When every edge weight is either **0 or 1**, a specialized algorithm called **0-1 BFS** can be used. Instead of a normal queue, it uses a **deque**. Edges with weight **0** are added to the front, while edges with weight **1** are added to the back. This allows it to find shortest paths efficiently without using Dijkstra's Algorithm.

---

## Q4: Which graph structures maximize BFS memory usage? (IMP)

**Answer:**

BFS uses the most memory on **wide graphs** that have many vertices at the same level. Since BFS stores an entire level of vertices in its queue before moving to the next level, graphs with a large branching factor require significantly more memory than deep, narrow graphs.

Example:

```
		  A
	  / / | \ \ 
	 B C D E F G
```

The queue may contain many nodes simultaneously.

---

## Q5: How does queue order affect traversal?

**Answer:**

BFS uses a **First-In, First-Out (FIFO)** queue. The first node added to the queue is the first one explored. This ensures that all vertices at the current level are visited before moving to the next level, which is why BFS performs a level-by-level traversal.

---

## Q6: How does graph density influence performance? (IMP)

**Answer:**

BFS always has a time complexity of **O(V + E)**, where **V** is the number of vertices and **E** is the number of edges.

In a **sparse graph**, there are relatively few edges, so BFS performs fewer neighbor checks.

In a **dense graph**, there are many more edges, so BFS must examine many more neighboring vertices. Although the time complexity remains **O(V + E)**, BFS performs more work because **E** is much larger.

---

## Q7: What metrics should be measured when benchmarking BFS against DFS, Dijkstra, and A*? (IMP)

**Answer:**

When comparing graph search algorithms, several metrics can be measured:

- Execution time
- Memory usage
- Number of nodes visited
- Number of edges explored
- Path length (number of edges)
- Total path cost (for weighted graphs)
- Path optimality
- Scalability as graph size increases
- Performance on sparse versus dense graphs

These metrics provide a fair comparison of both efficiency and solution quality.

---

## Q8: Why does BFS use a queue?

**Answer:**

BFS uses a queue because it follows the **First-In, First-Out (FIFO)** principle. This ensures that vertices are explored in the order they are discovered, allowing BFS to visit the graph level by level.

---

## Q9: Why can't BFS solve weighted shortest path problems?

**Answer:**

BFS ignores edge weights and assumes every edge has the same cost. It minimizes the number of edges rather than the total cost of the path. Therefore, it cannot guarantee the shortest weighted path.

---

## Q10: What happens if we remove the visited set?

**Answer:**

Without a visited set, BFS may repeatedly visit the same vertices. In graphs containing cycles, this can cause infinite loops and unnecessary repeated work, making the algorithm inefficient or unable to terminate.

---

## Q11: What is the difference between BFS and DFS?

**Answer:**

BFS explores the graph **level by level**, visiting all neighboring vertices before moving deeper into the graph. It uses a **queue**.

DFS explores one path as deeply as possible before backtracking and exploring another path. It uses a **stack** (either explicitly or through recursion).

---

## Q12: What is the time complexity?

**Answer:**

The time complexity of BFS is:

```
O(V + E)
```

where:

- **V** is the number of vertices.
- **E** is the number of edges.

Each vertex is visited once, and every edge is examined once.

---

## Q13: Can BFS detect cycles? (IMP)

**Answer:**

Yes, BFS can detect cycles, although DFS is more commonly used for this purpose.

In an **undirected graph**, BFS detects a cycle when it encounters a previously visited neighbor that is **not the current node's parent**.

In **directed graphs**, DFS is generally preferred because it naturally tracks the current recursion path, making cycle detection simpler.

---

## Q14: Why does BFS guarantee the shortest path?

**Answer:**

BFS guarantees the shortest path in an **unweighted graph** because it explores the graph **level by level**. The first time a vertex is reached, it is reached using the minimum possible number of edges. Since every edge has the same cost, this is also the shortest path.

## Q15: How does BFS work on disconnected graphs?

**Answer:**

BFS only explores the connected component that contains the starting vertex. Once the queue becomes empty, the algorithm terminates, even if other vertices exist elsewhere in the graph. Vertices that are not connected to the starting vertex remain unvisited.To traverse the entire graph, BFS must be restarted from every unvisited vertex. This approach is commonly used to identify connected components in a graph.

Example:

Component 1:

A — B — C


Component 2:

D — E

Starting BFS from A visits:

A → B → C

Vertices D and E remain unvisited because there is no path connecting them to A. To visit the entire graph, BFS must be run again starting from D (or any other unvisited vertex).

### Python Example

```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited.add(start)

    while queue:
        current = queue.popleft()
        print(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


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
        bfs(graph, node, visited) 
```

This approach ensures that every connected component is explored exactly once. Although BFS may be started multiple times, each vertex is still visited only once, so the overall time complexity remains **O(V + E)**.