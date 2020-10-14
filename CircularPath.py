for _ in range(int(input())):
    st = input()
    l,x,y = len(st),0,0
    direction = 'E'
    for i in range(l):
        if st[i]=='L' and direction=='E':
            direction = 'N'
        elif st[i]=='L' and direction=='N':
            direction = 'W'
        elif st[i]=='L' and direction=='W':
            direction = 'S'
        elif st[i]=='L' and direction=='S':
            direction = 'E'
        elif st[i]=='R' and direction=='E':
            direction = 'S'
        elif st[i]=='R' and direction=='S':
            direction = 'W'
        elif st[i]=='R' and direction=='W':
            direction = 'N'
        elif st[i]=='R' and direction=='N':
            direction = 'E'
        else:
            if direction=='E':
                x+=1
            elif direction=='W':
                x-=1
            elif direction=='N':
                y+=1
            else:
                y-=1
    if x==0 and y==0:
        print("CIRCULAR")
    else:
        print("NOT CIRCULAR")