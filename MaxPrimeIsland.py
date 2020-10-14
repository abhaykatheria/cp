from collections import defaultdict
primes = []
def sieve():
    n = 10**6 +1
    arr = [True]*n
    arr[0],arr[1],arr[2] = False, False,True
    for i in range(4,n,2):
        arr[i]=False
    for i in range(3,10**3 +1):
        if arr[i]==True:
            for j in range(i*i,n,i):
                if arr[j]==True:
                    arr[j]=False
    for i in range(n):
        if arr[i]:
            primes.append(i)

def dfs(src,visited,maxm):
    visited[src] = True
    maxm[0]+=1
    for negh in adj[src]:
        if not visited[negh]:
            dfs(negh,visited,maxm)

def dfs_main():
    visited = defaultdict(lambda:False)
    count = 0
    for src in keys:
        if not visited[src]:
            maxm = [0]
            dfs(src,visited,maxm)
            count = max(count,maxm[0])
    return count

sieve()
n,m =map(int,input().split())
adj = defaultdict(list)
keys = set()
for _ in range(m):
    u,v = map(int,input().split())
    adj[u].append(v)
    keys.add(u)
ans = dfs_main()
print(ans,primes[ans-1])
