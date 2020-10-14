def Shop(s,n,m,list1,list2):
    sum1=0
    list3=[]
    for i in range(0,n):
        for k in range(0,m):
            sum1=list1[i]+list2[j]
            list3.append(s-sum1)
            if sum1==s:
                print(sum1)
                break
            