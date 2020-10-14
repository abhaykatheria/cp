def cut_sticks(n,list1):
    l=len(list1)
    while l>1:
        minm=min(list1)
        l=len(list1)
        for i in range(0,l):
            list1[i] =list1[i]-minm  
        count=list1.count(0)
        for j in range(0,count):
            list1.remove(0)
        print(l)
        
n=int(input())
list1=list(map(int,input().split()))
cut_sticks(n,list1)