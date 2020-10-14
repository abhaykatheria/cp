#Shortest Path using BFS
from collections import defaultdict,deque
def neighbors(i,j,n,m,visited,mat):
    for x,y in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
        if x>=0 and x<n  and y>=0 and y<m and not visited[x][y] and mat[x][y]!=0:
            yield(x,y)

def bfs(mat,srcX,srcY,dstX,dstY,dist):
    visited = [[False for i in range(m)] for j in range(n)]
    visited[srcX][srcY] = True
    queue = deque([(srcX, srcY)])
    while queue:
        X,Y = queue.popleft()
        for x,y in neighbors(X,Y,n,m,visited,mat):
            visited[x][y] = True
            dist[x][y] = dist[X][Y]+1
            queue.append((x,y))

for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    mat = []
    temp = list(map(int,input().split()))
    i=0
    for j in range(n):
        mat.append(temp[i:i+m])
        i+=m
    srcX,srcY = 0,0
    dstX,dstY = map(int,input().split())
    if mat[srcX][srcY]==0 or mat[dstX][dstY]==0:
        print(-1)
    elif srcX==dstX and srcY==dstY:
        print(0)
    else:
        dist = [[0 for i in range(m)] for j in range(n)]
        bfs(mat,srcX,srcY,dstX,dstY,dist)
        print(dist[dstX][dstY] if dist[dstX][dstY] else -1)