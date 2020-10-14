# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 20:44:03 2020

@author: Mithilesh
"""

n , k = map(int,input().split())
arr = list(map(int,input().split()))
dp = [0,0]

dp[1] = abs(arr[1]-arr[0])

for i in range(2,n):
    minm = 10**18
    for j in range(1,k+1):
        if (i-j>=0):
            minm = min(minm,dp[i-j]+abs(arr[i]-arr[i-j]))
        else:
            break
    dp.append(minm)
print(dp[-1])