def sorting(list1):
    list1.sort()
    for c in list1:
        print(c,end=" ")
       
n=int(input())
list1=list(map(int,input().split()))
sorting(list1)