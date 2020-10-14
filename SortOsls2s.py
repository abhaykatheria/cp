for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    l = 0
    for i in range(n):
        if arr[i]==0:
            arr[i],arr[l] = arr[l],arr[i]
            l+=1
    for i in range(l,n):
        if arr[i]==1:
            arr[i],arr[l] = arr[l],arr[i]
            l+=1
    for ch in arr:
        print(ch,end=' ')
    print()