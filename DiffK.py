arr = list(map(int, input().split()))
k = int(input())
l,r = 0,1
while(l<len(arr) and r<len(arr)):
    diff = arr[r]-arr[l]
    if diff==k and r!=l:
        break
    elif diff>k:
        l+=1
    else:
        r+=1
if diff==k:
    print(1)
else:
    print(0)
