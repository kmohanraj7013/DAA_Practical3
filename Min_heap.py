import heapq

min_heap = []

# Insert
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 20)
heapq.heappush(min_heap, 1)

# Minimum element
print(min_heap[0])  # 1

# Remove minimum
print(heapq.heappop(min_heap))  # 1

print(min_heap)
