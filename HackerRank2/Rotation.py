def rotation(n,k,qu,arr):
    arr2=list(arr)
    temp=k%n
    for i in range(0,n):
        if (i+temp)<n:
            arr2[i+temp]=arr[i]
        else:
            arr2[(i+temp)-n]=arr[i]
    print(arr2[qu])

n,k,q=map(int,input().split())
arr=list(map(int,input().split()))
for p in range(0,q):
    qu=int(input())
    rotation(n,k,qu,arr)