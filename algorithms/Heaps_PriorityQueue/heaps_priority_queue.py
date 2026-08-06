import heapq

# --------------------
# Min-Heap Example
# --------------------

numbers = []

heapq.heappush(numbers, 7)
heapq.heappush(numbers, 3)
heapq.heappush(numbers, 10)
heapq.heappush(numbers, 1)

print("Min-Heap:")
print(numbers)

print("Smallest value:")
print(numbers[0])

removed_value = heapq.heappop(numbers)

print("Removed value:")
print(removed_value)

print("Heap after removal:")
print(numbers)

# --------------------
# Priority Queue Example
# --------------------

priority_queue = []

heapq.heappush(priority_queue, (3, "Complete assignment"))
heapq.heappush(priority_queue, (1, "Respond to emergency"))
heapq.heappush(priority_queue, (2, "Study graph algorithms"))

print("\nPriority Queue:")

while priority_queue:
    priority, task = heapq.heappop(priority_queue)
    print(priority, task)
