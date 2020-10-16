# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 22:28:04 2018

@author: Mithilesh
"""

def triplets(arr,tar):
    arr.sort()
    for i in range(len(arr)):
        if arr[i]>=tar-1:
            arr=arr[:i]
            break
    for i in range(len(arr)-2):
        for j in range(i+1,len(arr)-1):
            for k in range(j+1,len(arr)):
                if arr[i]+arr[j]+arr[k]==tar:
                    print(str(arr[i])+",",arr[j],"and",arr[k])
    
n=int(input())
arr=[]
for i in range(n):
    q=int(input())
    arr.append(q)
tar=int(input())
triplets(arr,tar)