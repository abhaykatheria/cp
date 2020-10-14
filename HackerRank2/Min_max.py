def min_max(list1):
    sum1,sum2,sum3,sum4,sum5=0,0,0,0,0
    for i in range(0,5):
        if i !=0:
            sum1=sum1+int(list1[i])
        if i !=1:
            sum2=sum2+int(list1[i])
        if i !=2:
            sum3=sum3+int(list1[i])
        if i !=3:
            sum4=sum4+int(list1[i])
        if i !=4:
            sum5=sum5+int(list1[i])
    z1=max(sum1,sum2,sum3,sum4,sum5)
    z2=min(sum1,sum2,sum3,sum4,sum5)
    print (z2,z1)
list1=list(map(int,input().split()))
min_max(list1)