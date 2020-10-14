def draw(n,p):
    count=-1
    if (n/2)>=p:
        for i in range(1,int(n/2)+1,2):
            if i==p or i-p==1:
                count +=1
                break
            else:
                count +=1
            
    else:
        if n%2!=0:
            for j in range(n,int(n/2),-2):
                if j==p or j-p==1:
                    count +=1
                    break
                else:
                    count +=1
        else:
            for j in range(n,int(n/2),-2):
                if j==p or p-j==1:
                    count +=1
                    break
                else:
                    count +=1            
    print(count)

n=int(input())
p=int(input())
draw(n,p)
        