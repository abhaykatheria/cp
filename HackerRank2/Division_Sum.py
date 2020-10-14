def Division_Sum(k,list1):
    count=0
    for i in range(0,n):
        for j in range(i+1,n):
            temp=list1[i]+list1[j]
            if temp%k==0:
                count +=1
                temp=0
            else:
                temp=0
    print(count)
    
n,k=map(int,input().split())
list1=list(map(int,input().split()))
Division_Sum(k,list1)