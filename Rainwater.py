for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    larr,rarr = [],[0 for i in range(n)]
    lmaxm,rmaxm = -10**18,-10**18
    for i in range(n):
        lmaxm = max(lmaxm,arr[i])
        larr.append(lmaxm)
    for i in range(n-1,-1,-1):
        rmaxm = max(rmaxm,arr[i])
        rarr[i] = rmaxm
    water = 0
    for i in range(n):
        water+=min(larr[i],rarr[i])-arr[i]
    print(water)