def PRINT(mat):
    for i in range(0,n):
        for j in range(0,n):
            print(mat[i][j],end=" ")
        print()

def matrix(n,m,k):
    mat=[[0 for i in range(n)] for j in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            if i==0 and j==0:
                mat[0][0]=m
            elif i==j:
                mat[i][j]=mat[i-1][j-1]+k
            elif i>j:
                mat[i][j]=mat[i-1][j]-1
            else:
                mat[i][j]=mat[i][j-1]-1
    PRINT(mat)
    
n,m,k=map(int,input().split())
matrix(n,m,k)
                