import collections
def isSafe():



n,m = map(int,input().split())
mat = []
for i in range(n):
    arr = list(map(int,input().split()))
    mat.append(arr)

queue = collections.deque([(0,0,0)])
visited = set()
visited.add((0,0))

while queue:
    steps,i,j = queue.popleft()
    if i==n-1 and j==m-1:
        break
    