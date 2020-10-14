def histogramArea(arr):
    ans = -10**18
    stack = []
    for i in range(len(arr)):
        if not stack or arr[stack[-1]]<=arr[i]:
            stack.append(i)
        else:
            while stack and arr[stack[-1]]>arr[i]:
                top = stack.pop()
                area = arr[top]*((i-stack[-1]-1) if stack else i )
                ans = max(area,ans)
            stack.append(i)
    while stack:
        top = stack.pop()
        area = arr[top]*((len(arr)-stack[-1]-1) if stack else len(arr) )
        ans = max(area,ans)
    return ans

def maxmLengthRectangle(m,n,mat):
    arr = [0]*n
    maxm_area = -10**18
    for i in range(m):
        for j in range(n):
            if mat[i][j]==0:
                arr[j]=0
            else:
                arr[j]+=(mat[i][j])
        maxm_area = max(maxm_area,histogramArea(arr))
    print(maxm_area)

m,n = map(int,input().split())
mat = []
for _ in range(m):
    t = list(map(int,input().split()))
    mat.append(t)

maxmLengthRectangle(m,n,mat)
