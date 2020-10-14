from collections import defaultdict
n = int(input())
arr = list(map(int,input().split()))
freq = defaultdict(int)
for ele in arr:
    freq[ele]+=1

stack = [0]
ans  = [-1]*n
for i in range(1,n):
    if freq[arr[i]]>freq[arr[stack[-1]]]:
        while stack and freq[arr[i]]>freq[arr[stack[-1]]]:
            ans[stack.pop()]=arr[i]
    stack.append(i)

print(arr)
print(ans)