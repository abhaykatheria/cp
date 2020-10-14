from collections import defaultdict
import heapq
st = input()
freq = defaultdict(int)
for ch in st:
    freq[ch]+=1
h=[]
count=0
for key in freq:
    heapq.heappush(h,-1*freq[key])
while(h):
    top = -1*heapq.heappop(h)
    if not h:
        break
    if top == -1*h[0]:
        if top>1:
            heapq.heappush(h,-1*(top-1))
        count+=1
print(count)