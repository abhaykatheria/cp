def jump(n,list1):
    count,k=0,0
    while k<n:
        if k+2<n:
            if list1[k]==0 and list1[k+1]==0 and list1[k+2]==0:
                count +=1
                k+=2
            elif list1[k]==0 and list1[k+1]==0 and list1[k+2]==1:
                count +=1
                k +=1
            elif list1[k]==0 and list1[k+1]==1 and list1[k+2]==0:
                count +=1
                k +=2
            else:
                continue
        else:
            if k+1==n-1:
                count +=1
            k +=1
            continue
    print(count)

n=int(input())
list1=list(map(int,input().split()))  
jump(n,list1)      
            