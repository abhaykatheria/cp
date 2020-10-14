def isSafe(mat,row,col,i,j,visited):
    if i>=0 and i<row and j>=0 and j<col and mat[i][j]==1 and visited[i][j]!=1:
        return True
    return False

def dfs(mat,row,col,i,j,visited):
    visited[i][j]=1
    rowNegh = [-1,-1,-1,0,0,1,1,1]
    colNegh = [-1,0,1,-1,1,-1,0,1]
    for k in range(8):
        if isSafe(mat,row,col,i+rowNegh[k],j+colNegh[k],visited):
            dfs(mat,row,col,i+rowNegh[k],j+colNegh[k],visited)

def countIslands(mat,row,col,visited):
    count = 0
    for i in range(row):
        for j in range(col):
            if(visited[i][j]!=1 and mat[i][j]==1):
                dfs(mat,row,col,i,j,visited)
                count+=1
    return count

row,col = map(int,input().split())
mat = []
for i in range(row):
    t = list(map(int,input().split()))
    mat.append(t)

visited = [[0 for _ in range(col)] for __ in range(row)]

ans = countIslands(mat,row,col,visited)
print(ans)
