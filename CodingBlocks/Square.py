# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:18:56 2019

@author: Mithilesh
"""

def square(n,d):
    start,end=0,n
    ans=-1
    while start<=end:
        mid=int((start+end)/2)
        if mid**2==n:
            ans=mid
            break
        elif mid**2<n:
            ans=mid
            start=mid+1
            
        elif mid**2>n:
            end=mid-1
    
    inc=0.1
    while d>0:
        while(ans*ans<=n):
            ans+=inc
        ans-=inc
        d-=1
        inc/=10
        
    return(ans)
print(square(24,3))  