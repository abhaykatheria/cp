def Compare(x1,v1,x2,v2):
    s1,s2,t=0,0,0
    while True:
        s1=x1+t*v1
        s2=x2+t*v2
        if s1==s2:
            flag=1
            break
        elif x1<x2 and v1<=v2:
            flag=0
            break
        elif s1<s2 and v1<=v2:
            flag=0
            break
        elif s1>s2 and v1>=v2:
            flag=0
            break
        else:
            t +=1
            continue
    if flag==1:
        print("YES")
    else:
        print("NO")
        
x1,v1,x2,v2=map(int,input().split())
Compare(x1,v1,x2,v2)