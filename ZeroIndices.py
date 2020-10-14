n = int(input())
arr = list(map(int,input().split()))
prefix = {0:[-1]}
som = 0
for i in range(n):
    som+=arr[i]
    if som in prefix.keys():
        for ind in prefix[som]:
            print(ind+1,i)
        prefix[som].append(i)
    else:
        prefix[som] = [i]
print(prefix)
