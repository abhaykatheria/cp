def grade(n,list1):
    quo=0
    temp1=0
    for i in range(0,n):
        if list1[i]%5 !=0 and list1[i]>37:
            quo=(list1[i]//5)+1
            temp1=quo*5
            if (temp1-list1[i])<3:
                list1[i]=temp1
            else:
                continue
        else:
            continue
    for i in range(0,n):
        print(list1[i])

n=int(input())
list1=[]
for i in range(0,n):
    temp=int(input())
    list1.append(temp)
grade(n,list1)




