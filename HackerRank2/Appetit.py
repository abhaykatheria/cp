def App(k,list1,b):
    temp,temp2=0,0
    list1[k]=0
    for j in range(0,n):
        temp2 +=list1[j]
    if temp2%2==0:
        temp2=temp2//2
    else:
        temp2=temp2/2
    if temp2==b:
        print("Bon Appetit")
    else:
        print(b-temp2)
n,k=map(int,input().split())
list1=list(map(int,input().split()))
b=int(input())
App(k,list1,b)