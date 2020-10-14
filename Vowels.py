strings = list(map(str,input().split()))
queries = list(map(str,input().split()))
n = len(strings)
prefix = [0]*(n+1)
som = 0
for i in range(n):
    if strings[i][0] in "aeiou":
        som+=1
    prefix[i+1] = som
print(prefix)
for query in queries:
    l,r = int(query[0]),int(query[-1])
    print(prefix[r]-prefix[l-1],end=" ")
