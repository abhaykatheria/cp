def squares(s,e):
    s1=int((s**0.5)//1)
    e1=int((e**0.5)//1)
    count=(e1-s1)//1
    if s**0.5%1==0 and e**0.5%1==0:
        count +=1
    elif s**0.5%1==0 and e**0.5%1!=0: 
        count +=1
    print(int(count))
q=int(input())
for qu in range(0,q):
    s,e=map(int,input().split())
    squares(s,e)
    
