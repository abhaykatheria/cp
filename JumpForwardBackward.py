def minDist(visited,dist,n):
    m = float('inf')
    res = 0
    for i in range(n):
        if not visited[i] and m>dist[i]:
            m = dist[i]
            res = i
    return res

def minimumSteps(arr,n):
    visited = [False]*n
    dist = [float('inf')]*n
    dist[0] = 0
    for i in range(n-1):
        u = minDist(visited,dist,n)
        visited[u] = True
        if u+2 <n and not visited[u+2] and dist[u]+arr[u+2]<dist[u+2]:
            dist[u+2] = arr[u+2] + dist[u]
        if u-1>=0 and not visited[u-1] and dist[u]+arr[u-1]<dist[u-1]:
            dist[u-1] = arr[u-1] + dist[u]
    print(dist)


n = int(input())
arr = list(map(int,input().split()))
print(minimumSteps(arr,n))
