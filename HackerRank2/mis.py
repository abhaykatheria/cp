s,t=map(int,input().split())
a,b=map(int,input().split())
m,n=map(int,input().split())
apple=list(map(int,input().split()))
orange=list(map(int,input().split()))
count1,count2=0,0
for i in range(0,m):
    if apple[i]<0:
        count1 +=0
    elif apple[i]>=(s-a) and apple[i]<=(t-a):
        count1 +=1
    else:
        continue
for j in range(0,n):
    if orange[j]>0:
        count2 +=0
    elif abs(orange[j])>=(b-t) and abs(orange[j])<=(b-s):
        count2 +=1
    else:
        continue
print(count1)
print(count2)