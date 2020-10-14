n,k = map(int,input().split())
arr = list(map(int,input().split()))
dp = [0]*n
dp[1] = abs(arr[1]-arr[0])

for i in range(2,n):
    minm = 10**18
    for j in range(1,k+1):
        if i-j>=0:
            minm = min(minm,dp[i-j]+abs(arr[i]-arr[i-j]))
        else:
            break
    dp[i] = minm
print(dp)