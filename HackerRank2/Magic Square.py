# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 22:58:39 2018

@author: Mithilesh
"""
import numpy as np
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr3=list(map(int,input().split()))
arr=np.stack((arr1,arr2,arr3),axis=0)
print(arr)
"""arr=list()
for i in range(3):
    row=list(map(int,input().split()))
    arr.append(row)
print(arr)"""
