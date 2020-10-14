def cellNumber(i,j,m):
    return(i*m+j)

def isSafe(row,col,r,c):
    if r>=0 and r<row and c>=0 and c<col:
        return True
    return False

mat = [[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,1,1,1,1,0,0,0],[0,1,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,0,1,0],[0,0,0,0,0,0,0,0,1,0]]

n,m = len(mat),len(mat[0])
k = int(input())

obs = 0
# for i in range(n):
#     t = list(map(int,input().split()))
#     mat.append(t)

adj = dict([(i,[]) for i in range(n*m)])
memory = [0]*(n*m)
for i in range(n):
    for j in range(m):
        memory[cellNumber(i,j,m)] = 'O' if mat[i][j]==1 else 'F'
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    for j in range(m):
        for de in range(4):
            if(isSafe(n,m,i+dx[de],j+dy[de])):
                adj[cellNumber(i,j,m)].append(cellNumber(i+dx[de],j+dy[de],m))

visited = [False]*(n*m)
distance = [0]*(n*m)
queue = []
visited[0] = True
queue.append(0)
dest = n*m-1
obs = 0

while(queue):
    node = queue[0]
    queue.pop(0)
    flag=0
    for negh in adj[node]:
        if memory[negh]=="O":
            obs+=1
            if(not visited[negh] and obs<=k):
                visited[negh] = True
                memory[negh] = 'F'
                distance[negh] = distance[node]+1
                if negh==dest:
                    flag=1
                    break
                queue.append(negh)
        else:
            if(not visited[negh]):
                visited[negh] = True
                distance[negh] = distance[node]+1
                if negh == dest:
                    flag=1
                    break
                queue.append(negh)

        if flag==1:
            break


print(distance)

