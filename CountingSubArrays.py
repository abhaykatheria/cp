n = int(input())
arr = list(map(int, input().split()))
prefix = [0]*len(arr)
count = 0
for i in range(len(arr)):
    som = 0
    for j in range(i,len(arr)):
        som+=arr[j]
        if som<n:
            count+=1
        else:
            break
print(count)