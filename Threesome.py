n,target = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
minm,min_sum = 10**18,10**18
for i in range(0,n-1):
    l,r,fixed = i+1,n-1,arr[i]
    while(l<r):
        som = fixed+arr[l]+arr[r]
        if som==target:
            min_sum = target
            break
        elif som<target:
            l+=1
            if minm > target-som:
                min_sum = som
                minm = target-som
        else:
            r-=1
            if minm > som-target:
                min_sum = som
                minm =som-target
    if min_sum==target:
        break
print(min_sum)
