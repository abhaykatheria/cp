# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 08:08:06 2019

@author: Mithilesh
"""

def sherlock(n,arr):
    lsum,rsum,flag,tsum=0,0,0,sum(arr)
    if n==1:
        print("YES")
    elif lsum==sum(arr[1:]) or rsum==sum(arr[-2::-1]):
        print("YES")
    elif n==2:
        lsum,rsum=sum(arr[:1]),sum(arr[1:])
        if lsum==rsum:
            print("YES")
        else:
            print("NO")
    else:
        for i in range(1,n-1):
            lsum+=arr[i-1]
            rsum=tsum-lsum-arr[i]
            if lsum==rsum:
                flag=0
                print("YES")
                break
            else:
                flag=1
        if flag==1:
            print("NO")
            
t=int(input())
for k in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    sherlock(n,arr)