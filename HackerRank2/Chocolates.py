def choco(n,c,m):
    sum1=0
    choc=n//c
    rappers,remainder=choc,0
    while choc>0:
        sum1 +=choc
        choc=rappers//m
        remainder=rappers%m
        rappers=choc+remainder
    print(sum1)

t=int(input())
for i in range(0,t):
    n,c,m=map(int,input().split())
    choco(n,c,m)