for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    for ele in arr:
        if abs(ele)-1<n-1:
            arr[abs(ele)-1] = -1*arr[abs(ele)-1]
    flag=0
    for i in range(n-1):
        if arr[i]>0:
            flag=1
            ans = i+1
    if flag==1:
        print(ans)
    else:
        print(n)
    