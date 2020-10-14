def cavity(n,q):
    for i in range(1,n-1):
        if int(q[i])>int(q[i+1]) and int(q[i])>int(q[i-1]) and q[i]!="X" and q[i-1]!="X" and q[i+1]!="X":
            q[i]="X"
        print(q)
    string=""
    for char in q:
        string=char+string
    print(string)
    
n=int(input())
for j in range(0,n):
    st=str(input())
    q=list(st)
    cavity(n,q)
    
        