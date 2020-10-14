def sock(n,arr):
    count=0
    lst=[]
    arr2=list(arr)
    arr=list(set(arr))
    for i in range(0,len(arr)):
        for j in range(0,n):
            if arr[i]==arr2[j]:
                count +=1
        lst.append(count)
        count=0
    sum1=0
    for k in range(0,len(lst)):
        sum1 +=lst[k]//2
    print(sum1)

n=int(input())
arr=list(map(int,input().split()))
sock(n,arr)