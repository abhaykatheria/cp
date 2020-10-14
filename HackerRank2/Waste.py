l=[1,2,3,4,1,1,4,5,1,1]
s=""
for c in l:
    s=str(c)+s
print(s)
p=s.count("1")
print(p)