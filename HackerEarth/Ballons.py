# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 22:01:55 2019

@author: Mithilesh
"""

t=int(input())
for q in range(t):
    g,p=map(int,input().split())
    n=int(input())
    tg,tp=0,0
    for i in range(n):
        gb,pb=map(int,input().split())
        tg+=gb
        tp+=pb
    total_cost=max(tg,tp)*min(g,p)+min(tg,tp)*max(g,p)
    print(total_cost)