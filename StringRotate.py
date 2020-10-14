n = int(input())
st = input()
st = "abcde"*10**5
n = 5*10**5
st+=st
dist = set()
for i in range(n):
    dist.add(st[i:i+n])
print(len(dist))