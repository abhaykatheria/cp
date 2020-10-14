def lcs(st1,st2):
    print(st1,st2)
    n = len(st1)
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if st1[i-1]==st2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    return(dp[n][n])


st = input()
print(len(st)-lcs(st,st[::-1]))
