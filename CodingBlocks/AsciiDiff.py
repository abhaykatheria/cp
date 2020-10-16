# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 23:23:50 2019

@author: Mithilesh
"""

string=input()
l=list(string)

for i in range(1,2*len(l)-1,2):
    l.insert(i,str(ord(l[i])-ord(l[i-1])))
print("".join(l))