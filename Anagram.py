from collections import defaultdict
def isAnagram(st1,st2):
    freq = defaultdict(lambda:0)
    for ch in st1:
        freq[ch]+=1
    for ch in st2:
        freq[ch]-=1
    for key in freq:
        if freq[key]!=0:
            return("NO")
    return("YES")

for _ in range(int(input())):
    st1,st2 = map(str,input().split())
    print(isAnagram(st1,st2))