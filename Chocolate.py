for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    arr.sort()
    minm = 10**18
    for i in range(0,n):
        if(i+m-1)>=n:
            break
        minm = min(minm,arr[i+m-1]-arr[i])
    print(minm)