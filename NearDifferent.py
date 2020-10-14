import heapq
from collections import defaultdict
n = int(input())
st = input()
freq  = defaultdict(int)
for ch in st:
    freq[ch]+=1
max_heap = []
for key in freq:
    heapq.heappush(max_heap,(-1*freq[key],key))

prev = (1,"#")
ans = ""
while max_heap:
    freq,char=heapq.heappop(max_heap)
    freq*=-1
    ans+=char
    if -1*prev[0]>0:
        heapq.heappush(max_heap,(prev))
    freq-=1
    prev = (-freq,char)


print(ans if len(ans)==n else "Not Possible ")
    