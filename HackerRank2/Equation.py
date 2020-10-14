def Equation(n,p):
    p.insert(0,0)
    for x in range(1,n+1):
        for i in range(1,n+1):
            if x==p[i]:
                print(p.index(i))
            else:
                continue
    
n=int(input())
p=list(map(int,input().split()))
Equation(n,p)