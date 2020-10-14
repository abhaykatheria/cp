from collections import defaultdict
from functools import cmp_to_key

def compare(val1,val2):
    print("Comapring ",(val1,freq[val1]),(val2,freq[val2]))
    if freq[val1]==freq[val2]:
        return(val1-val2)
    return(freq[val2]-freq[val1])

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    freq = defaultdict(int)
    for ch in arr:
        freq[ch] +=1
    for ch in sorted(freq,key=cmp_to_key(compare)):
        for i in range(freq[ch]):
            print(ch,end=' ')
    print()

