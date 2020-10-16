# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 22:41:40 2018

@author: Mithilesh
"""
def city_tour(s,x,di):
    key=list(di.keys())
    if 1 in key:
        continue
    else:
        di[1]=x
        key.append(1)
    key.sort()
    sum1,days=di.get(1),1
    l=len(key)
    while True:
        for j in range(0,l):
            if sum1>=s:
                print(days)
                break
            else:
                sum1+=(key[j+1]-key[j]))*x+di.get(key[j+1])
                if sum1>s:
                    temp=(s-sum1)
                    
                    
       
        

s,x,n=map(int,input().split())
di=dict(map(int,input().split()) for i in range(n))
