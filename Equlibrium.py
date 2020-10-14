for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    lsum,rsum,l,r,flg=arr[0],arr[-1],0,n-1,0
    if n==1:
        print(1)
    else:
        while(l<r):
            if lsum==rsum and l+2==r:
                flg=1
                print(l+2)
                break
            elif lsum>rsum:
                r-=1
                rsum+=arr[r]
            elif lsum<rsum:
                l+=1
                lsum+=arr[l]
            else:
                l+=1
                r-=1
                lsum+=arr[l]
                rsum+=arr[r]
        
        if flg==0:
            print(-1)