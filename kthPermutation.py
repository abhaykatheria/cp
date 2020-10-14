n = int(input())
k = int(input())
k=k-1
numbers = [i+1 for i in range(n)]
indices = [0]*n
div = 1
for i in range(1,n+1):
    if k//div==0:
        break
    else:
        indices[n-i] = (k//div)%i
        div*=i

for i in range(n):
    index = indices[i]+i
    if index !=i:
        temp = numbers[index]
        for j in range(index,i,-1):
            numbers[j] = numbers[j-1]
        numbers[i] = temp

print(numbers)


