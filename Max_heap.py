import heapq

max_heap = []

# Insert
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -20)
heapq.heappush(max_heap, -1)

# Maximum element
print(-max_heap[0])  # 20

# Remove maximum
print(-heapq.heappop(max_heap))  # 20

# Print heap as normal values
print([-x for x in max_heap])
