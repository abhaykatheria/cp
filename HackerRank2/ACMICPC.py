# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 07:13:20 2019

@author: Mithilesh
"""

def acmteam(n,m,topic):
    count=[]
    for i in range(n-1):
        st=topic[i]
        for j in range(i+1,n):
            te=topic[j]
            cou=0
            for k in range(m):
                if (st[k]=='1' or te[k]=='1'):
                    cou+=1
            count.append(cou)
    print(max(count),count.count(max(count)))
    
n,m=map(int,input().split())
topic=[]
for t in range(n):
    ch=str(input())
    topic.append(ch)
acmteam(n,m,topic)