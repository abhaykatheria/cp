#Cycle Using BFS

from collections import defaultdict,deque
def detectCycleBFS(adjaceny):
    parent = defaultdict(int)
    visited = defaultdict(lambda:False)
    for node in adjaceny:
        parent[node] = node
        visited[node] = False
    src = 1
    queue = deque()
    queue.append(src)
    visited[src] = True
    while queue:
        node = queue.popleft()
        for negh in adjaceny[node]:
            if not visited[negh]:
                visited[negh] = True
                parent[negh] = node
                queue.append(negh)
            else:
                if parent[node] != negh:
                    return True
    return False

n,e = map(int,input().split())
adjaceny = defaultdict(list)
for _ in range(e):
    u,v = map(int,input().split())
    adjaceny[u].append(v)
    adjaceny[v].append(u)

if (detectCycleBFS(adjaceny)):
    print("Cycle is present")
else:
    print("Cycle is not present")

