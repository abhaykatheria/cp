n ,k = map(int,input().split())
arr = list(map(int,input().split()))
l,r,zero_count,best_window,best_left=0,0,0,0,0
while(r<n):
    if zero_count<=k:
        if arr[r]==0:
            zero_count+=1
        r+=1
    if zero_count>k:
        if arr[l]==0:
            zero_count-=1
        l+=1
    if r-l > best_window:
        best_left = l
        best_window = r-l

print(arr[best_left:best_left+best_window])