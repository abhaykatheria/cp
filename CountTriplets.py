for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    triplets=0
    for i in range(n-1,1,-1):
        target = arr[i]
        l,r=0,i-1
        while(l<r):
            if arr[l]+arr[r]==target:
                triplets+=1
                l+=1
                r-=1
            elif arr[l]+arr[r]>target:
                r-=1
            else:
                l+=1
    if triplets==0:
        print(-1)
    else:
        print(triplets)