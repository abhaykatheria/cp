n = int(input())
mat = []
for i in range(n):
    arr = list(map(int,input().split()))
    mat.append(arr)
a,b=0,n-1
while(a<b):
    if mat[a][b]:
        a+=1
    else:
        b-=1
flag=0
for i in range(n):
    if i==a:
        continue
    elif not mat[i][a] or mat[a][i]:
        flag=1
        break 

if flag==1:
    print("Not Celeb")
else:
    print(c+1,"is the celebrity")
