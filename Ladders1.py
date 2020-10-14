n,k = map(int,input().split())
arr = list(map(int,input().split()))
dp = [0]*(n+1)
dp[1]=1
for i in range(2,n+1):
    if arr[i-1]!=1:
        for j in range(1,k+1):
            if i-j>=1:
                dp[i]+=dp[i-j]
            else:
                break

print(dp[-1])

