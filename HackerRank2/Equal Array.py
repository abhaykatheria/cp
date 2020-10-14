def array(n,arr):
    count=0
    lst=[]
    arr2=list(arr)
    arr=list(set(arr))
    print(arr)
    for i in range(0,len(arr)):
        for j in range(0,n):
            if arr[i]==arr2[j]:
                count +=1
        lst.append(count)
        count=0
    maxm=max(lst)
    sum1=0
    for k in range(0,len(lst)):
        sum1 +=lst[k]
    print(sum1-maxm)

n=int(input())
arr=list(map(int,input().split()))
array(n,arr)