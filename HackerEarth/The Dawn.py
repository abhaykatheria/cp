# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 23:16:20 2018

@author: Mithilesh
"""

def dawn(n):
    sum1,minm=0,n
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            sum1=(n//i)+i
            if sum1<minm:
                minm=sum1
    print(minm)

n=int(input())
dawn(n)