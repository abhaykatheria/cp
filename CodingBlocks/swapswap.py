# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:48:05 2019

@author: Mithilesh
"""

def swap_swap(n,k,arr) :
    for i in range(n-1) :  
        if (k > 0):
            index = i 
            for j in range(i + 1, n):
                if (k <= j - i): 
                    break
                if (arr[j] > arr[index]): 
                    index = j
            for j in range(index, i, -1): 
                arr[j-1],arr[j]=arr[j],arr[j-1]
            k = k - index - i 
    for i in range(n):
        print(arr[i],end=" ")

n,k=map(int,input().split())
arr=list(map(int,input().split()))
swap_swap(n,k,arr)