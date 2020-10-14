def jump(x,d,N,list1):
    count=0
    maxm=max(list1)
    for i in range(x,maxm+1,d):
        if i in list1:
            count +=1
    print (count)
    
x,d,N=map(int,input().split())
list1=list(map(int,input().split()))
jump(x,d,N,list1)
        