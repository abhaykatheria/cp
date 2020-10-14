# All Unique Window

from collections import defaultdict
st1 = input()
st2 = input()
main_freq = defaultdict(int)
second_freq = defaultdict(int)
l1,l2 = len(st1),len(st2)
for ch in st2:
    second_freq[ch]+=1
start,start_index,count,minm_window = 0,-1,0,float('inf')
for i in range(l1):
    main_freq[st1[i]]+=1

    if second_freq[st1[i]] and main_freq[st1[i]]<=second_freq[st1[i]]:
            count+=1
    if count==l2:
        while main_freq[st1[start]]>second_freq[st1[start]] or not second_freq[st1[start]]:
            if main_freq[st1[start]]>second_freq[st1[start]]:
                main_freq[st1[start]]-=1
            start+=1
        len_window = i - start + 1
        if minm_window > len_window:
            minm_window = len_window
            start_index = start
print(st1[start_index:start_index+minm_window] if start_index!=-1 else "No such window")

