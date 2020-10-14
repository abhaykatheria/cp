n = int(input())
arr = list(map(int, input().split()))
dp = [0]*(n+1)

for i in range(1,n+1):
    maxm = -10**18
    for j in range(1,i+1):
        maxm = max(maxm,arr[j-1]+dp[i-j])
    dp[i] = maxm

print(dp[-1])