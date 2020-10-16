# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 03:36:36 2018

@author: Mithilesh
"""

def update(ID,val,arr,n):
    ID-=1
    while val!=0:
        if ID<n:
            arr[ID]+=val
            if arr[ID]>10**9:
                arr[ID]%=10**9+7
        else:
            ID=0
            arr[0]+=val
            if arr[0]>10**9:
                arr[0]%=10**9+7
        ID+=1
        val-=1
    return(arr)
    
def query(l,r,arr,n):
    if l<r:
        return((sum(arr[l-1:r]))%(10**9 + 7))
    elif l==r:
        return(arr[l-1])
    else:
        return((sum(arr)-sum(arr[r:l-1]))%(10**9 + 7))

n,q=map(int,input().split())
arr=list(map(int,input().split()))
for t in range(q):
    qt,a,b=map(int,input().split())
    if qt==1:
        arr=update(a,b,arr,n)
    else:
        ans=query(a,b,arr,n)
        print(ans)