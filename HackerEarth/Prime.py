# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 15:19:36 2018

@author: Mithilesh
"""
import math
def prime(n):
    flag=0
    print(2,3,end=" ")
    for i in range(5,n+1):
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                flag=0
                break
            else:
                flag=1
                continue
        if flag==1:
            flag=0
            print(i,end=" ")

n=int(input("Enter the number: "))
prime(n)
