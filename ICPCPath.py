from collections import defaultdict
import heapq

def dijsktras(src,adjecency,n):
    dist = [10**18]*n
    dist[src] = 0
    h = []
    heapq.heappush(h,(0,src))
    while(h):
        currCost,currVertex = heapq.heappop(h)
        for negh,neghCost in adjecency[currVertex]:
            if currCost + neghCost < dist[negh]:
                dist[negh] = currCost + neghCost
                heapq.heappush(h,(dist[negh],negh))
    return(dist)
