from collections import defaultdict,deque

def minPath(src):
    dist = defaultdict(int)
    visited = defaultdict(lambda:False)
    queue = deque()
    queue.append(src)
    while queue:
        src = queue.popleft()
        visited[src]= True
        for negh in adj[src]:
            if not visited[negh]:
                visited[negh]=True
                dist[negh] = dist[src]+1
                queue.append(negh)
    return dist

n,m = map(int,input().split())
adj = defaultdict(list)
for _ in range(m):
    u,v=map(int,input().split())
    adj[u].append(v)
print(minPath(1))