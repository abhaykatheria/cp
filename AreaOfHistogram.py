n = int(input())
arr = list(map(int,input().split()))
stack = []
maxm_area = -10**18
for i in range(n):
    if not stack or arr[stack[-1]]<=arr[i]:
        stack.append(i)
    else:
        while stack and arr[stack[-1]]>arr[i]:
            top = stack.pop()
            area = arr[top]*((i-stack[-1]-1) if stack else i)
            maxm_area=max(area,maxm_area)
        stack.append(i)
while stack :
        top = stack.pop()
        area = arr[top]*((n-stack[-1]-1) if stack else n)
        maxm_area=max(area,maxm_area)
print(maxm_area)