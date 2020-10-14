for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    boolArr = [0 for i in range(n)]
    minm,maxm = arr[-1],arr[0]
    for i in range(n-2,0,-1):
        if arr[i]<=minm:
            boolArr[i]=1
            minm = arr[i]
    for i in range(1,n-1):
        if arr[i]>=maxm:
            if boolArr[i]:
                boolArr[i]=1
            maxm = arr[i]
        else:
            boolArr[i]=0
    f=0
    for i in range(n):
        if boolArr[i]:
            f=1
            print(arr[i])
            break
    if f==0:
        print(-1)
