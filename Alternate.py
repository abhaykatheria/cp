for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    if n==1:
        print(arr[0])
    else:
        arr[0],arr[n-1]=arr[n-1],arr[0]
        arr[1],arr[n-1]=arr[n-1],arr[1]
        l,r = 2,n-2
        while(l<r):
            arr[l],arr[r] = arr[r],arr[l]
            arr[l+1],arr[r+1] = arr[r+1],arr[l+1]
            l+=2
            r-=1
        arr[n-2],arr[n-1] = arr[n-1],arr[n-2]
        for ch in arr:
            print(ch,end=' ')
        
