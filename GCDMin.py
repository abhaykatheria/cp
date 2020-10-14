for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    minm = min(arr)
    hashed = [False]*n
    div= []
    for i in range(n):
        if arr[i]%minm==0:
            hashed[i] = True
            div.append(arr[i])
    div.sort()
    j=0
    temp = list(arr)
    for i in range(n):
        if hashed[i]==True:
            arr[i] = div[j]
            j+=1
    temp.sort()
    if temp==arr:
        print("YES")
    else:
        print("NO")
