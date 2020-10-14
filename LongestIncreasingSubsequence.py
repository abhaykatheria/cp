def LIS(n,arr):
    dp = [1]*n
    i = 1
    while i < n:
        for j in range(i):
            if arr[j]<arr[i]:
                dp[i]=dp[j]+1
        i+=1
    print(dp)

n = int(input())
arr = list(map(int,input().split()))
LIS(n,arr)