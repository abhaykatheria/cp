from collections import defaultdict
n, target = map(int,input().split())
arr = list(map(int,input().split()))

sum_freq = defaultdict(lambda :0)
som,count = 0,0
for i in range(n):
    som+=arr[i]
    if som == target:
        count+=1
    if (som-target) in sum_freq:
        count+=sum_freq[som-target] 
    sum_freq[som]+=1

print(sum_freq)

print(count)
