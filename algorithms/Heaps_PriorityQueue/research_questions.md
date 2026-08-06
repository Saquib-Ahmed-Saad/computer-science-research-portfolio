# Research Questions

## Fundamental Concepts

- What is the difference between a heap and a priority queue?
- Why is a heap considered a complete binary tree?
- Why is a heap stored as an array instead of using tree nodes?
- What is the difference between a min-heap and a max-heap?
- Why is a heap only partially sorted?

---

## Heap Operations

- How does insertion maintain the heap property?
- How does removal of the root maintain the heap property?
- Why does insertion take O(log n) time?
- Why does deletion take O(log n) time?
- Why does accessing the root take O(1) time?
- Why does building a heap from an existing list take O(n) instead of O(n log n)?
- What is the purpose of heapify?

---

## Python Implementation

- Why does Python provide only a min-heap in the `heapq` module?
- How can a max-heap be implemented using `heapq`?
- Why are tuples commonly stored inside a priority queue?
- What happens when two elements have the same priority?
- Why does `heapq.heappush()` automatically maintain the heap property?
- Why does the printed heap not appear fully sorted?

---

## Comparisons

- What is the difference between a heap and a binary search tree?
- When should a heap be used instead of a sorted list?
- What are the advantages of a priority queue over a normal queue?
- When is using a heap unnecessary?

---

## Applications

- Why does Dijkstra's algorithm require a priority queue?
- Why does A* use a priority queue?
- How are heaps used in operating systems?
- How are heaps used in CPU scheduling?
- How are heaps used in event simulation?
- How are heaps used in Huffman coding?
- How are heaps used to merge multiple sorted arrays?

---

## Advanced Exploration

- Can a heap efficiently search for arbitrary values?
- What happens if duplicate values exist inside a heap?
- How would a priority queue behave if priorities change after insertion?
- What are Fibonacci Heaps, and why are they faster for some algorithms?
- What are Binomial Heaps, and how do they compare to Binary Heaps?
- Why are Fibonacci Heaps rarely used in practice despite better theoretical complexity?
- How does heap performance change as the number of elements grows?
- What are the trade-offs between binary heaps, Fibonacci heaps, and pairing heaps?
