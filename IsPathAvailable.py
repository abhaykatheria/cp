# from collections import defaultdict

# def neighbors(i,j,n,visited,mat):
#     for x,y in (i,j-1),(i,j+1),(i-1,j),(i+1,j):
#         if x>=0 and x<n and y>=0 and y<n and not visited[x][y] and mat[x][y]!=0:
#             yield(x,y)

# def dfs(mat,srcX,srcY,visited):
#     visited[srcX][srcY] = True
#     for x,y in neighbors(srcX,srcY,n,visited,mat):
#         visited[x][y] = True
#         dfs(mat,x,y,visited)

# n = int(input())
# mat = []
# visited = [[False for _ in range(n)] for __ in range(n)]
# for i in range(n):
#     arr = list(map(int, input().split()))
#     mat.append(arr)
# srcX,srcY = map(int,input().split())
# dfs(mat,srcX,srcY,visited)
# print(visited)


from collections import defaultdict

def neighbors(i,j,n,visited,mat):
    for x,y in (i,j-1),(i,j+1),(i-1,j),(i+1,j):
        if x>=0 and x<n and y>=0 and y<n and not visited[x][y] and mat[x][y]!=0:
            yield(x,y)

def dfs(mat,srcX,srcY,visited):
    visited[srcX][srcY] = True
    for x,y in neighbors(srcX,srcY,n,visited,mat):
        visited[x][y] = True
        dfs(mat,x,y,visited)
for _ in range(int(input())):
    n = int(input())
    mat = []
    arr = list(map(int, input().split()))
    visited = [[False for _ in range(n)] for __ in range(n)]
    i=0
    for j in range(n):
        mat.append(arr[i:i+n])
        i+=n
    print(mat)
    for i in range(n):
        for j in range(n):
            if mat[i][j]==1:
                srcX,srcY=i,j
            if mat[i][j]==2:
                dstX,dstY=i,j
    dfs(mat,srcX,srcY,visited)
    if visited[dstX][dstY]:
        print(1)
    else:
        print(0)
    
    
    
