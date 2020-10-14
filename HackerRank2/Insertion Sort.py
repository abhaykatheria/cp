def print_(list1):
    for c in list1:
        print(c,end=" ")
    print()

def insertion(n,list1):
    for i in range(2,n+1):
        list2=list1[0:i]
        if i<n:
            list1=list1[i:]
        else:
            list1.clear()
        list2.sort()
        list1=list2+list1
        print_(list1)

n=int(input())
list1=list(map(int,input().split()))
insertion(n,list1)
                
        