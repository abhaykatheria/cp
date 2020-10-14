def lane(n,list1,s,e):
    minm=min(list1[s:e+1])
    print(minm)

n,t=map(int,input().split())
list1=list(map(int,input().split()))
for i in range(0,n):
    s,e=map(int,input().split())
    lane(n,list1,s,e)