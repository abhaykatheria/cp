from collections import deque,defaultdict

def dfs(src,visited,path):
    visited[src] = True
    for negh in adj[src]:
        if not visited[negh]:
            dfs(negh,visited,path)
    path.append(src)
def dfs_main():
    visited = defaultdict(lambda:False)
    path = []
    for src in list(adj):
        if not visited[src]:
            dfs(src,visited,path)
    return path[::-1]

adj = defaultdict(list)
for _ in range(int(input())):
    u,v = map(int,input().split())
    adj[u].append(v)
print(dfs_main())