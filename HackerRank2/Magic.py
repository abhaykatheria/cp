def magic(n,k,list1):
    maxm=max(list1)
    if maxm>k:
        count=maxm-k
    else:
        count=0
    print(count)

n,k=map(int,input().split())
list1=list(map(int,input().split()))
magic(n,k,list1)