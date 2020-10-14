def calc_matrix(n,matrix):
    sum1,sum2=0,0
    for i in range(0,n):
        for j in range(0,n):
            if i==j:
                sum1=sum1+matrix[i][j]
            if (i+j)==n-1:
                sum2=sum2+matrix[i][j]
            else:
                continue
    print(abs(sum1-sum2))
n=int(input())
matrix=[]
for i in range(0,n):
    element=[int(i) for i in input().split()]
    matrix.append(element)
calc_matrix(n,matrix)
    