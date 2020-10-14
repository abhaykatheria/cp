def FAN(n,d,list1):
    notifications=0
    median=0
    for i in range(0,n-d):
        list2=list1[i:i+d]
        list2.sort()
        if d%2==0:
            median=(list2[(d-2)//2] + list2[(d)//2])/2
        else:
            median=list2[(d-1)//2]
        if list1[i+d]>=2*median:
            notifications +=1
    print(notifications)

n,d=map(int,input().split())
list1=list(map(int,input().split()))
FAN(n,d,list1)