# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 19:08:40 2018

@author: Mithilesh
"""

def partition(arr,start,end):
    pivot,index=arr[start],start+1              
    for i in range(start+1,end+1):          
        if arr[i]<=pivot:
            arr[i],arr[index]=arr[index],arr[i]
            index+=1
    arr[start],arr[index-1]=arr[index-1],arr[start]
    for ch in arr:
        print(ch,end=" ")
    print()
    
n=int(input())
arr=list(map(int,input().split()))
partition(arr,0,n-1)