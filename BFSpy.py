from collections import defaultdict , deque

def BFS(n,adjacency):
    queue = deque()
    queue.append(src)
    dist = [0 for i in range(n)]
    visited = [False]*n
    visited[src] = True
    while(len(queue)):
        currVertex = queue.popleft()
        print(currVertex,end="-->")
        for negh in adjacency[currVertex]:
            if not visited[negh]:
                visited[negh] = True
                dist[negh] = dist[currVertex]+1
                queue.append(negh)
    return(dist)

    
n,e = map(int,input().split())
adjacency = defaultdict(list)
for i in range(e):
    u,v = map(int,input().split())
    adjacency[u].append(v)
    #adjacency[v].append(u)
print(adjacency)
src = int(input())
print(BFS(n,adjacency))

