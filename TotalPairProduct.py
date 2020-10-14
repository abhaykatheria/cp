n,k = map(int,input().split())
arr = list(map(int,input().split()))
l,r = 0,n-1
ans = 0
while(l<r):
    if arr[l]*arr[r]<k:
        ans+=(r-l)
        l+=1
    else:
        r-=1
print(ans)