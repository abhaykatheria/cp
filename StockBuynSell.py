for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    profit = [0 for i in range(n)]
    for i in range(n-2,-1,-1):
        if arr[i+1]-arr[i]>0:
            profit[i] = arr[i+1]-arr[i] + profit[i+1]
    l,f=0,0
    while(l<n):
        if profit[l]!=0:
            r=l+1
            f=1
            while(profit[r]!=0 and r<n):
                r+=1
            print('('+str(l)+' '+str(r)+')',end=' ')
            l=r
        else:
            l+=1
    if f==0:
        print("No Profit")
    else:
        print()
