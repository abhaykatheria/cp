def cats(x,y,z):
    if abs(z-x)>abs(y-z):
        print("Cat B")
    elif abs(z-x)<abs(y-z):
        print("Cat A")
    else:
        print("Mouse C")

q=int(input())
for i in range(0,q):
    x,y,z=map(int,input().split())
    cats(x,y,z)