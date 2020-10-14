def median(n,list1):
    ind=(n-1)//2
    list1.sort()
    print(list1[ind])
    
n=int(input())
list1=list(map(int,input().split()))
median(n,list1)