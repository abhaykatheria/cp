n = int(input())
A,B,C = [],[],[]
for i in range(n):
    a,b,c = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)

dpA,dpB,dpC = [0]*n,[0]*n,[0]*n
dpA[0],dpB[0],dpC[0] = A[0],B[0],C[0]

for i in range(1,n):
    dpA[i] = max(dpB[i-1],dpC[i-1])+A[i]
    dpB[i] = max(dpA[i-1],dpC[i-1])+B[i]
    dpC[i] = max(dpB[i-1],dpA[i-1])+C[i]

print(max(dpA[-1],dpB[-1],dpC[-1]))