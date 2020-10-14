for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    square = [arr[i]**2 for i in range(n)]
    square.sort()
    f=0
    #%%
    for i in range(n-1,-1,-1):
        l,r=0,i-1
        while(l<r):
            if square[l]+square[r]==square[i]:
                f=1
                break
            elif square[l]+square[r]>square[i]:
                r-=1
            else:
                l+=1
        if f==1:
            print("Yes")
            break
    if f==0:
        print("No")

