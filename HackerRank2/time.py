def time(n,k,list1):
    count_early=0
    for j in range(0,n):
        if list1[j]<=0:
            count_early +=1
        else:
            continue
    print(count_early)
    if count_early>=k:
        print("NO")
    else:
        print("YES")

t=int(input())
for i in range(0,t):
    n,k=map(int,input().split())
    list1=list(map(int,input().split()))
    time(n,k,list1)    