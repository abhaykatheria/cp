def sort(l):
    l.sort()
    for a in l:
        print(a)

n=int(input())
l=[]
for i in range(0,n):
    q=int(input())
    l.append(q)
sort(l)