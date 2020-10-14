def insertion(n,list1):
    temp=0
    list2=list(list1)
    list2.sort()
    count=0
    while True:
        for i in range(0,n):
            if i+1<n and list1[i]>list1[i+1]:
                temp=list1[i+1]
                list1[i+1]=list1[i]
                list1[i]=temp
                count +=1
        if list2==list1:
            break
    print(count)
    
q=int(input())
for i in range(0,q):
    n=int(input())
    list1=list(map(int,input().split()))
    insertion(n,list1)