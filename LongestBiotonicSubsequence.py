def LIS(n,arr):
    i=1
    dp = [1]*n
    while(i<n):
        for j in range(i):
            if arr[j]<arr[i]:
                dp[i]=dp[j]+1
        i+=1
    return dp

n = int(input())
arr = list(map(int,input().split()))
d1 = LIS(n,arr)
d2 = LIS(n,arr[::-1])
ans = d1[0]+d2[0]-1
for i in range(1,n):
    ans = max(d1[i]+d2[i]-1,ans)
print(ans)