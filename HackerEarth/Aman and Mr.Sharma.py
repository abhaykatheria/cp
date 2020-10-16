# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 15:04:23 2018

@author: Mithilesh
"""
d=int(input())
toffee=0
for i in range(0,d):
    r,x=map(int,input().split())
    pie=(22/7)
    run=100*x
    perimeter=2*pie*r
    if run>=perimeter:
        toffee+=1
print(toffee)
