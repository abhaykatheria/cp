def cellNumber(i,j,col):
    return(i*col+j)

def isSafe(mat,row,col,r,c):
    if r>=0 and r<row and c>=0 and c<col and mat[r][c]!='B':
        return True
n,m = map(int,input().split())
mat = []
dis = []
for i in range(n):
    temp = list(input())
    mat.append(temp)
adj = dict([(i,[]) for i in range(n*m)])
dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = [[0 for  i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        if mat[i][j]=="E":
            src = cellNumber(i,j,m)
        if mat[i][j]=="B":
            ans[i][j]=-1
        else:
            for k in range(4):
                if (isSafe(mat,n,m,i+dx[k],j+dy[k])):
                    adj[cellNumber(i,j,m)].append(cellNumber(i+dx[k],j+dy[k],m))
        
        

queue = []
distance = [0]*(n*m)
visited = [False]*(n*m)
queue.append(src)
visited[src] = True
while(queue):
    node = queue.pop(0)
    for negh in adj[node]:
        if(not visited[negh]):
            visited[negh] = True
            distance[negh] = distance[node]+1
            queue.append(negh)

for i in range(n):
    for j in range(m):
        loc = cellNumber(i,j,m)
        if ans[i][j] != -1:
            if loc==src:
                ans[i][j] = 0
            elif distance[loc]==0:
                ans[i][j] = -1
            else:
                ans[i][j] = distance[loc]


for i in range(n):
    for j in range(m):
        print(ans[i][j],end=" ")
    print()





CBBC
BBCC
CECC
CCCC



