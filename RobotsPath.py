for _ in range(int(input())):
    n,m = map(int,input().split())
    mat = []
    for i in range(n):
        arr = list(map(int,input().split()))
        mat.append(arr)
    
    dp = [[0 for i in range(m)] for j in range(n)]
    for i in range(m):
        if mat[0][i]==0:
            break
        else:
            dp[0][i] =1
    for i in range(n):
        if mat[i][0]==0:
            break
        else:
            dp[i][0]=1
    
    for i in range(1,n):
        for j in range(1,m):
            if mat[i][j]==0:
                continue
            else:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
    print(dp)
    print(dp[n-1][m-1])

