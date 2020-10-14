def AC(st):
    deletion=0
    for i in range(0,len(st)):
        if i+1<len(st):
            if (st[i]=="A" and st[i+1]=="B") or (st[i]=="B" and st[i+1]=="A"):
                deletion +=0
            elif (st[i]=="A" and st[i+1]=="A") or (st[i]=="B" and st[i+1]=="B"):
                deletion +=1
    print(deletion)

n=int(input())
for qu in range(0,n):
    st=str(input())
    AC(st)