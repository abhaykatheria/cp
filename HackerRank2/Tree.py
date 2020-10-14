def height(n):
    h=1
    k=0
    while k!=n:
        if k%2==0:  
            h=2*h
            k +=1
        else:
            h +=1
            k +=1
    print(h)

t=int(input())
for i in range(0,t):
    n=int(input())
    height(n)