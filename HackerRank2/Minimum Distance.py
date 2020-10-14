def minimum(n,arr):
    d=0
    lst=[]
    count=0
    arr2=list(set(arr))
    for i in range(0,n):
        d=0
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                d=abs(j-i)
                lst.append(d)
                break
    arr2.sort()
    arr.sort()
    if arr2==arr:
        print("-1")
    else:
        minm=min(lst)
        print(minm)

n=int(input())
arr=list(map(int,input().split()))
minimum(n,arr)