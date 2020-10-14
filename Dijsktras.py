#Dijktras
import heapq
from collections import defaultdict
def dijsktras(graph,src,dist):
    record = []
    heapq.heappush(record,(0,src))
    while(len(record)):
        currCost, currVertex = heapq.heappop(record)
        for negh, neghCost in graph[currVertex]:
            if currCost + neghCost < dist[negh]:
                heapq.heappush(record,(neghCost+currCost, negh))
                dist[negh] = currCost + neghCost
    return(dist)

for _ in range(int(input())):
    graph = defaultdict(list)
    dist = defaultdict(list)
    m,n = map(int,input().split())
    for i in range(m):
        u,v,cost = map(str,input().split())
        graph[u].append((v,int(cost)))
        graph[v].append((u,int(cost)))
    src = input()
    for key in graph:
        dist[key] = 10**18
    dist[src] = 0
    dijsktras(graph,src,dist)
    for key in dist:
        if dist[key]==10**18:
            print(-1,end=" ")
        else:
            print(dist[key],end=" ")
    print()
# 9 9
# A B 10
# A C 3
# B C 1
# C B 4
# B D 2
# C D 8
# C E 2
# D E 7
# E D 9
