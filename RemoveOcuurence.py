for _ in range(int(input())):
    st1 = input()
    st2 = input()
    s1,n1,n2 = list(st1),len(st1),len(st2)
    i,count= 0,0
    while(i<n1):
        if (i+n2>n1):
            break
        if(i<0):
            i=0
        t = "".join(s1[i:i+n2])
        if t==st2:
            count+=1
            s1 = s1[:i]+s1[i+n2:]
            i-=(n2+2)
            n1 = len(s1)
        else:
            i+=1
    print(count)