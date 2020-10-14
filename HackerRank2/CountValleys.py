def Count_Valleys(n,list1):
    count,sum1=0,0
    list2=[]
    for i in range(0,n):
        if list1[i]=="U":
            list1[i]=1
            sum1+=list1[i]
            list2.append(sum1)
        else:
            list1[i]=-1
            sum1+=list1[i]
            list2.append(sum1)
            
    for j in range(0,n-1):
        if list2[j]==-1 and list2[j+1]==0:
            count+=1
            
    print(count)
    
n=int(input())
list1=list(input())
Count_Valleys(n,list1)