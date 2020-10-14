def number(n,arr):
    count=0
    lst=[]
    for i in range(0,100):
        for j in range(0,n):
            if i==arr[j]:
                count +=1
        lst.append(count)
        count=0
    for c in lst:
        print(c,end=" ")
    print()
n=int(input())
arr=list(map(int,input().split()))
number(n,arr)