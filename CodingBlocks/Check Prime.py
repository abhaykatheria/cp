# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 16:04:42 2018

@author: Mithilesh
"""

def check_prime(n):
    flag=0
    if n in [2,3]:
        print("Prime")
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                print("Not Prime")
                flag=0
                break
            else:
                flag=1
    if flag==1:
        print("Prime")
    
n=int(input())
check_prime(n)