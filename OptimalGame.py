def optimalGame(dp,arr,l,r,som):
    if l+1 == r:
        return(max(arr[l],arr[r]))
    if dp[l][r]!=-1:
        return(dp[l][r])
    dp[l][r]=(max(som - optimalGame(dp,arr,l+1,r,som-arr[l]),som - optimalGame(dp,arr,l,r-1,som-arr[r])))
    return(dp[l][r])

n = int(input())
arr = list(map(int,input().split()))
dp = [[-1 for _ in range(n)] for j in range(n)]
print(optimalGame(dp,arr,0,n-1,sum(arr)))