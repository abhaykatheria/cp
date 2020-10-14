def area(list1,string1):
    temp=0
    list2=list("abcdefghijklmnopqrstuvwxyz")
    list3=[]
    for char in string1:
        for i in range(0,len(list2)):
            if char==list2[i]:
                temp=list2.index(char)
                list3.append(list1[temp])
            else:
                continue
    maxm=max(list3)
    area=maxm*len(string1)
    print(area)

list1=list(map(int,input().split()))
string1=str(input())
area(list1,string1)
                
                