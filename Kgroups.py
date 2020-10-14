for _ in range(int(input())):
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(0,n,k):
        l,r=i,i+k-1
        if r>=n:
            r=n-1
        while(l<=r):
            arr[l],arr[r] = arr[r],arr[l]
            l+=1
            r-=1
    for ch in arr:
        print(ch,end=' ')
    print()
