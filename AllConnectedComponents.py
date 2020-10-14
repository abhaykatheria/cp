#All COnnected Components
from collections import defaultdict
def dfs(src,visited,lst):
    visited[src] =True
    lst.append(src)
    for negh in adj[src]:
        if not visited[negh]:
            dfs(negh,visited,lst)

def dfs_main():
    visited = defaultdict(lambda:False)
    components = []
    count=0
    for key in keys:
        if not visited[key]:
            lst=[]
            dfs(key,visited,lst)
            components.append(lst)
            count+=1
    return components

n,m = map(int,input().split())
adj = defaultdict(list)
keys = set()
for _ in range(m):
    u,v = map(int,input().split())
    adj[u].append(v)
    keys.add(u)
print(dfs_main())