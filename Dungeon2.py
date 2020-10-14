import collections
def isSafe(mat,row,col,r,c,visited):
    for x,y in (r-1,c),(r+1,c),(r,c-1),(r,c+1):
        if x>=0 and x<row and y>=0 and y<col and mat[x][y]!="B" and (x,y) not in visited:
            yield(x,y)
n,m = map(int,input().split())
mat,f,dist = [],0,[[-1 for i in range(m)] for j in range(n)]
for i in range(n):
    temp = list(input())
    mat.append(temp)
for i in range(n):
    for j in range(m):
        if mat[i][j]=='E':
            srcX,srcY=i,j
            dist[i][j]=0
            f=1
            break
    if f==1:
        break
queue = collections.deque([(0,srcX,srcY)])
visited = set()
visited.add((srcX,srcY))
while queue:
    steps,i,j = queue.popleft()
    for x, y in isSafe(mat,n,m,i,j,visited):
        dist[x][y]=steps+1
        queue.append((steps+1,x,y))
        visited.add((x,y))
print(dist)

