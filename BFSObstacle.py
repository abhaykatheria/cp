#Remove K Obstacle

import collections
def validNeighbors(mat,i,j, obstacleCount,visited):
    for x, y in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
        if x>=0 and x<n and y>=0 and y<m:
            newObsCount = obstacleCount + mat[x][y]
            if newObsCount<=k and (x,y,newObsCount) not in visited:
                yield (x,y,newObsCount)
mat = []
n,m = len(mat),len(mat[0])
k = int(input())
ans = -1
for i in range(n):
    t = list(map(int,input().split()))
    mat.append(t)
queue = collections.deque([(0,0,0,0)]) #steps, i, j , obstacleCount
visited = set()
visited.add((0,0,0))  #i,j, obstacleCount

while queue:
    steps,i,j,obstacleCount = queue.popleft()
    if i==n-1 and j==m-1:
        ans = steps
        break

    for x,y,oc in validNeighbors(mat,i,j,obstacleCount,visited):
        queue.append([steps+1,x,y,oc])
        visited.add((x,y,oc))

print(ans)