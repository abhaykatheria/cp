def cloud(n,k,cl):
    E=100
    for i in range(0,n,k):
        if cl[i]==0:
            E -=1
        else:
            E=E-2-1
    print(E)

n,k=map(int,input().split())
cl=list(map(int,input().split()))
cloud(n,k,cl)