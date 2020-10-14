# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 01:16:11 2017

@author: Mithilesh
"""

def choco(n,list1,d,m):
    sum1,count=0,0
    for i in range(0,n):
        sum1=0
        if (i+m)<=n:
            for j in range(i,i+m):
                    sum1 +=list1[j]
            if sum1==d:
                count +=1
    print(count)
                
n=int(input())
list1=list(map(int,input().split()))
d,m=map(int,input().split())
choco(n,list1,d,m)