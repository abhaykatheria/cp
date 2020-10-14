def check(n,list1):
    list2=[]
    sum1=0
    for v in list1:
        list2.append(list1.count(v))
        list1.remove(v)
        print(list1)
    for i in range(0,len(list2)):
        sum1 +=list2[i]
    print(list2)
    print(sum1)
    print(sum1-max(list2))
n=int(input())
list1=list(map(int,input().split()))
check(n,list1)        