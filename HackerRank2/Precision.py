def precision(n,list1):
    count_positive,count_negative,count_zero=0,0,0
    for i in list1:
        if i>0:
            count_positive +=1
        elif i<0:
            count_negative +=1
        else:
            count_zero +=1
    print (count_positive/n)
    print (count_negative/n)
    print (count_zero/n)
n=int(input())
list1=list(map(int,input().split()))
precision(n,list1)