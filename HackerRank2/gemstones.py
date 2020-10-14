def gem_stones(n,list1):
    arr=set.intersection(*map(set,list1))
    print(len(arr))
    
n=int(input())
list1=[]
for i in range(0,n):
    string=str(input())
    lis=list(string)
    list1.append(lis)
    
gem_stones(n,list1)