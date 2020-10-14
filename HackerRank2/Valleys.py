def count(steps,string):
    count,count1,t=0,0,0
    v=[]
    v1=[]
    for i in range(0,steps):
        if string[i]=="U":
            count +=1
            v.append(str(count))         
        else:
            count -=1
            v.append(str(count))
    v1=list(v)
    while len(v)!=0:
        z=v1.index("-1")
        v=v[z:]
        if len(v)>0 and v[0]==-1:
            if "0" in v:
                count1 +=1
                print(v)
                v=v[v.index("0"):]
                break
        
    print(abs(count1))

steps=int(input())
string=str(input())
count(steps,string)