def close(n,list1):
    list1.sort()
    min_diff=list1[1]-list1[0]
    list2=[]
    for i in range(0,n-1):
        diff=0
        diff=list1[i+1]-list1[i]
        if diff<=min_diff:
            if diff==min_diff:
                list2.append(list1.index(list1[i]))
                list2.append(list1.index(list1[i+1]))
            else:                
                list2.clear()
                list2.append(list1.index(list1[i]))
                list2.append(list1.index(list1[i+1]))
            min_diff=diff
    
    l=len(list2)
    for j in range(0,l):
        print(list1[list2[j]],end=" ")
        
n=int(input())
list1=list(map(int,input().split()))
close(n,list1)
            
            
            