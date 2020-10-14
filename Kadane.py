for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    som,maxm = 0,-10**18
    for i in range(n):
        som+=arr[i]
        maxm = max(som,maxm)
        if som<0:
            som=0 
    print(maxm)