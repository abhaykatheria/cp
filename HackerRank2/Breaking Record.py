def record(n,list1):
    maxm=list1[0]
    minm=list1[0]
    max_count,min_count=0,0
    for i in range(1,n):
        if list1[i]>maxm:
            max_count +=1
            maxm=list1[i]
        elif list1[i]<minm:
            min_count +=1
            minm=list1[i]
        else:
            continue
    print(max_count,min_count)
    
n=int(input())
list1=list(map(int,input().split()))
record(n,list1)