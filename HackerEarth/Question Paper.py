# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 00:36:52 2018

@author: Mithilesh
"""

def question_paper(n,a,b):
    arr=[]
    if a==b:
        print(2*n+1)
    else:
        for i in range(0,n+1):
            for j in range(0,n+1):
                if (n-i-j>=0):
                    arr.append(j*a-(n-i-j)*b)
        print(len(set(arr)))

t=int(input())
for q in range(t):
    n,a,b=map(int,input().split())
    question_paper(n,a,b)