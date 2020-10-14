n = int(input())
arr = list(map(int,input().split()))
stack = [0]
ans = [-1]*n
for i in range(1,n):
    if arr[i]<arr[stack[-1]]:
        stack.append(i)
    else:
        while(stack and arr[i]>arr[stack[-1]]):
            print(arr[stack[-1]], "-->", arr[i])
            stack.pop()
        stack.append(i)

while(len(stack)>0):
    print(arr[stack[-1]], "-->", -1)
    stack.pop()