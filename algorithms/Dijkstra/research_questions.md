# Research Questions

## Fundamental Concepts

- What problem does Dijkstra's Algorithm solve?
- Why does Dijkstra require weighted graphs?
- Why are non-negative edge weights required?
- What is meant by the shortest path?
- Why are all initial distances set to infinity?

---

## Algorithm

- Why is the starting node assigned a distance of zero?
- Why is a priority queue used instead of a normal queue?
- Why is the node with the smallest distance always explored first?
- What is edge relaxation?
- Why can a node's distance change multiple times before being finalized?
- What does it mean when a node is finalized?

---

## Negative Edges

- Why do negative edge weights break Dijkstra's Algorithm?
- Can Dijkstra sometimes work correctly even with negative edges?
- Why is Dijkstra no longer guaranteed to be correct when negative edges exist?
- Which algorithm should be used instead of Dijkstra for graphs with negative edges?

---

## Comparisons

- How does Dijkstra differ from BFS?
- How does Dijkstra differ from DFS?
- How does Dijkstra differ from Bellman-Ford?
- When should Dijkstra be preferred over A*?
- Why is Dijkstra considered a greedy algorithm?

---

## Applications

- How does GPS use Dijkstra's Algorithm?
- How do navigation systems handle changing road conditions?
- How do computer networks use shortest-path algorithms?
- How do robots use Dijkstra for path planning?
- Why is Dijkstra useful in logistics and delivery optimization?

---

## Advanced Exploration

- What happens if a new road is added after Dijkstra has finished?
- Why does rerunning Dijkstra solve the problem?
- What are dynamic shortest-path algorithms?
- How does graph density affect Dijkstra's performance?
- Why does using a binary heap improve efficiency?
- What is the difference between binary heaps and Fibonacci heaps in Dijkstra?
- Can Dijkstra optimize multiple objectives such as cost and distance?
- How would Dijkstra behave if every edge had the same weight?
