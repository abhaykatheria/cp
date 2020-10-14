def encryption(st):
    l=len(st)
    string=""
    if (l)**0.5%1!=0:
        n=(-1+(1+4*1*l)**0.5)/2
        n1=round(n)
        n2=n1+1
        for i in range(0,n1+1):
            for j in range(i,l,n2):
                string=string+st[j]
            string +=" "        
    else:
        n=l**0.5
        n1=int(n)
        n2=int(n)
        for i in range(0,n1):
            for j in range(i,l,n2):
                string=string+st[j]
            string +=" "
    print(string)

st=str(input())
encryption(st)
