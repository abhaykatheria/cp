for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    for i in range(1,n,2):
        if i!=n-1:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    for ch in arr:
        print(ch,end=' ')
    print()