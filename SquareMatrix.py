def longestSqaureMatrix(m,n,mat):
    grid = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if mat[i-1][j-1]:
                grid[i][j]=min(grid[i-1][j-1],grid[i-1][j],grid[i][j-1])+1
    for row in grid:
        print(row)

m,n = map(int,input().split())
mat = []
for _ in range(m):
    t = list(map(int,input().split()))
    mat.append(t)
longestSqaureMatrix(m,n,mat)

# 4 5
# 0 0 1 1 1
# 1 0 1 1 1
# 0 1 1 1 1
# 1 0 1 1 1