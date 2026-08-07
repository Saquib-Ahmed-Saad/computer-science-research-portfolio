# Heaps and Priority Queues

## Overview

### Q1: What is a heap?

Ans: A heap is a tree-based data structure that keeps its smallest or largest element at the top.

There are two main types of heaps:

- Min-Heap: The smallest value is stored at the root.
- Max-Heap: The largest value is stored at the root.

A heap is commonly represented using a Python list rather than explicitly creating tree nodes.

---

### Q2: What is a priority queue?

Ans: A priority queue is a data structure where elements are removed according to their priority rather than the order in which they were added.

In a normal queue, the first item added is the first item removed.

In a priority queue, the item with the highest priority is removed first.

Python's `heapq` module implements a min-heap, so the item with the smallest priority value is removed first.

---

## Heap Structure

A min-heap follows this rule:

> Every parent node must be smaller than or equal to its children.

Example:

```text
        2
       / \
      4   5
     / \
    8   10
```

The smallest value, `2`, is stored at the root.

A heap does not completely sort every value. It only guarantees that the smallest value is always available at the root.

---

## Array Representation

A heap can be stored inside a list.

For a node stored at index `i`:

```text
Left child  = 2i + 1
Right child = 2i + 2
Parent      = (i - 1) // 2
```

Example:

```python
heap = [2, 4, 5, 8, 10]
```

This list represents:

```text
        2
       / \
      4   5
     / \
    8   10
```

---

## Data Structures Used

- A list to store the heap
- The `heapq` module to maintain heap order
- Tuples for storing priority-value pairs in a priority queue

---

## Common Heap Operations

### `heapq.heappush()`

Adds an item to the heap while maintaining the heap property.

### `heapq.heappop()`

Removes and returns the smallest item from the heap.

### `heapq.heapify()`

Converts an existing list into a valid heap.

### Accessing the smallest item

The smallest item can be viewed using:

```python
heap[0]
```

This does not remove it.

---

## Python Implementation

```python
import heapq


# Create an empty min-heap
numbers = []

# Add values to the heap
heapq.heappush(numbers, 7)
heapq.heappush(numbers, 3)
heapq.heappush(numbers, 10)
heapq.heappush(numbers, 1)

print("Heap:", numbers)

# View the smallest value
print("Smallest value:", numbers[0])

# Remove the smallest value
smallest = heapq.heappop(numbers)

print("Removed:", smallest)
print("Heap after removal:", numbers)
```

Possible output:

```text
Heap: [1, 3, 10, 7]
Smallest value: 1
Removed: 1
Heap after removal: [3, 7, 10]
```

The list may not appear completely sorted, but it still follows the min-heap property.

---

## Priority Queue Implementation

```python
import heapq


priority_queue = []

heapq.heappush(priority_queue, (3, "Complete assignment"))
heapq.heappush(priority_queue, (1, "Respond to emergency"))
heapq.heappush(priority_queue, (2, "Study graph algorithms"))

while priority_queue:
    priority, task = heapq.heappop(priority_queue)
    print(priority, task)
```

The output would be:

```text
1 Respond to emergency
2 Study graph algorithms
3 Complete assignment
```

The task with the smallest priority number is removed first.

---

## Code Walkthrough

### 1. `import heapq`

The `heapq` module provides the functions required to create and manage a min-heap in Python.

---

### 2. `numbers = []`

An empty list is created to store the heap.

---

### 3. `heapq.heappush(numbers, value)`

This adds a new value to the heap.

Python automatically moves the value into the correct position so that the smallest value remains at the root.

---

### 4. `numbers[0]`

The value at index `0` is always the smallest value in a Python min-heap.

This operation only views the smallest value. It does not remove it.

---

### 5. `heapq.heappop(numbers)`

This removes and returns the smallest value from the heap.

After removal, Python reorganizes the heap to preserve the heap property.

---

### 6. `(priority, task)`

A priority queue can store tuples.

Python first compares the first item in each tuple, which is the priority.

For example:

```python
(1, "Emergency")
(2, "Study")
(3, "Assignment")
```

The tuple with priority `1` will be removed first.

---

### 7. `while priority_queue:`

The loop continues until every item has been removed from the priority queue.

---

## Time Complexity

| Operation | Time Complexity |
|---|---:|
| View smallest item | O(1) |
| Insert an item | O(log n) |
| Remove smallest item | O(log n) |
| Convert list into heap | O(n) |

Here, `n` represents the number of elements stored in the heap.

Insertion and removal take `O(log n)` because an element may need to move upward or downward through the height of the heap.

---

## Why are heaps useful?

A heap allows us to repeatedly access the smallest or largest item efficiently.

Without a heap, finding the smallest item in an unsorted list could take `O(n)` time.

With a min-heap, the smallest value is always located at index `0`, so it can be accessed in `O(1)` time.

---

## Applications

- Dijkstra's shortest-path algorithm
- A* search
- Task scheduling
- CPU scheduling
- Event simulation
- Finding the smallest or largest values
- Merging sorted collections
- Huffman coding

---

## Limitations

- A heap is not completely sorted.
- Searching for an arbitrary value still takes O(n) time.
- Python's `heapq` directly supports min-heaps, not traditional max-heaps.
- Items with equal priorities may require an additional tie-breaking value.
- Changing the priority of an existing item is not always straightforward.

---


