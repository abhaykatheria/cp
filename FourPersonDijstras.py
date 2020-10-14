#Four Person Dijsktras
from collections import defaultdict
import heapq

def cellNumber(i,j,m):
    return(i*m+j)

def isSafe(x,y,n):
    if x>=0 and x<n and y>=0 and y<n:
        return True
    return False
def dijsktras(n,adjacency,src):
    h = []
    dist = [10**18]*(n*n)
    dist[src] = 0
    heapq.heapify(h)
    heapq.heappush(h,(0,src))   #inserting cost and src

    while(len(h)):
        currCost,currVertex = heapq.heappop(h)
        for negh in adjacency[currVertex]:
            if 1 + currCost < dist[negh]:
                heapq.heappush(h,(1+currCost,negh))
                dist[negh] = 1 + currCost
    return(dist)
n = int(input())
src1,src2,src3,src4 = map(int,input().split())

dx = [1,-1,0,0]
dy = [0,0,-1,1]
adjacency = defaultdict(list)
for i in range(n):
    for j in range(n):
        cell = cellNumber(i,j,n)
        for k in range(4):
            if isSafe(i+dx[k],j+dy[k],n):
                adjacency[cell].append(cellNumber(i+dx[k],j+dy[k],n))
d1,d2,d3,d4 = dijsktras(n,adjacency,src1),dijsktras(n,adjacency,src2),dijsktras(n,adjacency,src3),dijsktras(n,adjacency,src4)
df = [(d1[i]+d2[i]+d3[i]+d4[i],i) for i in range(n*n)]
df.sort()
print(df[0])
# print(d1)
# print(d2)
# print(d3)
# print(d4)


