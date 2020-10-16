# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 03:38:34 2018

@author: Mithilesh
"""

def multiple(n):
    sum3,sum5,sum15=0,0,0
    k3,k5,k15=n//3,n//5,n//15
    if n%3!=0:
        sum3=(k3/2)*(2*3+(k3-1)*3)
    else:
        sum3=((k3-1)/2)*(2*3+(k3-2)*3)
    if n%5!=0:
        sum5=(k5/2)*(2*5+(k5-1)*5)
    else:
        sum5=((k5-1)/2)*(2*5+(k5-2)*5)
    if n%15!=0:
        sum15=(k15/2)*(2*15+(k15-1)*15)
    else:
        sum15=((k15-1)/2)*(2*15+(k15-2)*15)
    print(sum3,sum5,sum15)
    print(sum3+sum5-sum15)

t=int(input())
for q in range(t):
    n=int(input())
    multiple(n)