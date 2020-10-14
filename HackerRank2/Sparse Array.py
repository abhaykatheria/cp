# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 03:17:26 2018

@author: Mithilesh
"""

def sparse_array(n,q,str1,que1):
    for i in range(0,q):
        print(str1.count(que1[i]))
    
n=int(input())
str1=[]
que1=[]
for j in range(0,n):
    str1_elements=str(input())
    str1.append(str1_elements)
q=int(input())
for k in range(0,q):
    que1_elements=str(input())
    que1.append(que1_elements)
    
sparse_array(n,q,str1,que1)