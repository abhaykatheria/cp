from collections import deque
def safeNegh(x,y):
    for nx,ny in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
        if nx>=0 and nx<n and ny>=0 and ny<m and mat[nx][ny]==1:
            yield nx,ny

def bfs():
    queue = deque()
    maxm = -1
    for i in range(n):
        for j in range(m):
            if mat[i][j]==2:
                queue.append((0,i,j))  #time,x,y

    while(queue):
        time,x,y = queue.popleft()
        for nx,ny in safeNegh(x,y):
            queue.append((time+1,nx,ny))
            maxm = max(maxm,time+1)
            mat[nx][ny]=2
    return maxm

n,m = map(int,input().split())
mat = []
for _ in range(n):
    arr = list(map(int,input().split()))
    mat.append(arr)
ans = bfs()
flag=0
for i in range(n):
    for j in range(m):
        print(mat[i][j],end=" ")
        if mat[i][j]==1:
            flag=1
    print()
if flag:
    print(-1)
if ans ==-1:
    print(0)
# 3 5
# 2 1 0 2 1
# 1 0 1 2 1
# 1 0 0 2 1