from heapq import heapify,heappush,heapreplace,heappop
arr = [11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45]
k = 3
heap = []
for i in range(k):
    heappush(heap,arr[i])
print(heap)
for i in range(k,len(arr)):
    if arr[i]>heap[0]:
        heapreplace(heap,arr[i])

print([heappop(heap) for i in range(k)])