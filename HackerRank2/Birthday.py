def birthday(b,w,x,y,z):
    cost=0
    if (x+z<y):
        cost=(b*x)+(w*(x+z))
    elif (y+z<x):
        cost=(b*(y+z)+(w*y))
    else:
        cost=(b*x)+(w*y)
    print(cost)
    
t=int(input())
for i in range(0,t):
    b,w=map(int,input().split())
    x,y,z=map(int,input().split())
    birthday(b,w,x,y,z)