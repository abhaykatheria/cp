from collections import defaultdict
import heapq

def dijstras():
    pass

n,m = map(int,input().split())
grid = []
for _ in range(m):
    arr = list(map(int,input().split()))
    grid.append(arr)