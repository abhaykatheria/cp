# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:57:44 2018

@author: Mithilesh
"""
n,qu=map(int,input().split())
seqlist=[[] for i in range(n)]
last_answer=0
for t in range(qu):
    q,x,y=map(int,input().split())
    if q==1:
        seq=((x^last_answer)%n)
        seqlist[seq].append(y)
    else:
        seq=((x^last_answer)%n)
        size=len(seqlist[seq])
        last_answer=seqlist[seq][y%size]
        print(last_answer)