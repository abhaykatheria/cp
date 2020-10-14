for _ in range(int(input())):
    p,f = map(int,input().split())
    cs,cw = map(int,input().split())
    s,w = map(int,input().split())
    if(max(p,f)//min(s,w)+min(p,f)//max(s,w)>=cs+cw):
        print(cs+cw)
    else:
        t1 = max(p,f)//min(s,w)
        t2 = min(p,f)//max(s,w)
        r1 = max(p,f)%min(s,w)
        r2 = min(p,f)%max(s,w)
        ans = t1+t2
        r = r1+r2