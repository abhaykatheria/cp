from collections import defaultdict
from functools import cmp_to_key
def compare(e1,e2):
    if e1[1]==e2[1]:
        return len(e1[0])-len(e2[0])
    return e1[1]-e2[1]

def dfs(src,dest,visited,path,cost):
    visited[src]=True
    path.append((src,cost))
    if src == dest:
        temp = list(path)
        p,c="",0
        for e in temp:
            c+=e[1]  
            p+=e[0]+" "
        paths.append((p.rstrip(),c))
    else:
        for negh,cost in adj[src]:
            if not visited[negh]:
                dfs(negh,dest,visited,path,cost)
    path.pop()
    visited[src]=False

def dfs_main():
    visited = defaultdict(lambda:False)
    path = []
    cost = 0
    dfs(src,dest,visited,path,cost)

n = int(input())
adj = defaultdict(list)
for _ in range(n):
    u,v,c = map(str,input().split())
    adj[u].append((v,int(c)))
paths = []
src,dest = "Entrance","Vault"
dfs_main()
paths = sorted(paths,key=cmp_to_key(compare))
for path, cost in paths:
    print(path,cost)

