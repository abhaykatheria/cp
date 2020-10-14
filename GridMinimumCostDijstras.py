#Grid Dijsktras
import heapq
from collections import defaultdict

def cellNumber(i,j,m):
    return(i*m+j)

def isSafe(x,y,n):
    if x<n and y<n and x>=0 and y>=0:
        return True
    return False

def dijsktras(adjacency,src,dist):
    h = []
    heapq.heappush(h,(0,src))
    while(len(h)):
        currCost, currVertex = heapq.heappop(h)
        for negh,neghCost in adjacency[currVertex]:
            if neghCost + currCost < dist[negh]:
                heapq.heappush(h,(neghCost + currCost,negh))
                dist[negh] = neghCost + currCost
        
n = int(input())
arr = list(map(int,input().split()))
dx = [0,0,1,-1]
dy = [1,-1,0,0]
adjacency = defaultdict(list)
dist  = defaultdict(int)
for i in range(n*n):
    dist[i] = 10**18
dist[0] = 0
for i in range(n):
    for j in range(n):
        for k in range(4):
            if isSafe(i+dx[k],j+dy[k],n):
                adjacency[cellNumber(i,j,n)].append((cellNumber(i+dx[k],j+dy[k],n),arr[cellNumber(i+dx[k],j+dy[k],n)]))
dijsktras(adjacency,0,dist)
print(dist[n*n-1]+arr[0])