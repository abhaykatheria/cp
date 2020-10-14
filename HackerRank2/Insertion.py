def insertion(n,list1):
    temp=list1[n-1]
    i=n-2
    while True:
        if i>=0 and temp<list1[i]:
            list1[i+1]=list1[i]
            i -=1
            for a in list1:
                print(a,end=" ")
            print()
        else:
            list1[i+1]=temp
            for a in list1:
                print(a,end=" ")
            print()
            break
    
n=int(input())
list1=list(map(int,input().split()))
insertion(n,list1)