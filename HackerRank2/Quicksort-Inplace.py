# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 18:48:42 2018

@author: Mithilesh
"""
def quicksort(arr):
    quicksort2(arr,0,len(arr)-1)
    return(arr)

def partition(arr,start,end):
    arr2=list(arr)
    arr2.sort()      
    pivot,index=arr[end],start              
    for i in range(start,end):          
        if arr[i]<=pivot:
            arr[i],arr[index]=arr[index],arr[i]
            index+=1
    arr[end],arr[index]=arr[index],arr[end]
    if arr!=arr2:
        for ch in arr:
            print(ch,end=" ")
        print()
    return(index)

def quicksort2(arr,start,end):
    if start<end:
        index=partition(arr,start,end)
        quicksort2(arr,start,index-1)
        quicksort2(arr,index+1,end)
    return(arr)
n=int(input())
arr=list(map(int,input().split()))
start,end=0,len(arr)
sorted_array=quicksort(arr)
for ch in sorted_array:
    print(ch,end=" ")