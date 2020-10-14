def func(l,u):
    count=0
    for i in range(l,u+1):
        sq1=i**2
        sq=str(sq1)
        le=len(sq)
        if le !=1:
            sum1=int(sq[0:(le//2):])+int(sq[le//2::])
            if sum1==i:
                print(i,end=" ")
                count+=1
    if count==0:
        print("INVALID RANGE")

def kaprekar(l,u):
    if l==1:
        print("1",end=" ")
        func(l,u)
        
    else:
        func(l,u)
        
l=int(input())
u=int(input())
kaprekar(l,u)

    