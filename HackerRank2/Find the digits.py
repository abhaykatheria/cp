def count(n):
    string=str(n)
    list1=list(string)
    count=0
    for i in range(0,len(list1)):
        if int(list1[i])!=0 and n%int(list1[i])==0:
            count +=1
        else:
            continue
    print(count)

t=int(input())
for k in range(0,t):
    n=int(input())
    count(n)