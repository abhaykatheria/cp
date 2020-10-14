from collections import defaultdict

def dfs(src,visited,stack):
    visited[src]=True
    stack[src]=True

    for negh in adj[src]:
        if stack[negh]:
            return True
        if not visited[negh] and dfs(negh,visited,stack):
            return True
    stack[src]=False
    return False

def dfs_main():
    visited = defaultdict(lambda: False)
    stack = defaultdict(lambda:False)

    for src in list(adj):
        if not visited[src]:
            ans = dfs(src,visited,stack)
    return ans

n,m = map(int,input().split())
adj = defaultdict(list)
for _ in range(m):
    u,v = map(int,input().split())
    adj[u].append(v)
print("Yes cycle is there" if dfs_main() else "No cycle is there")