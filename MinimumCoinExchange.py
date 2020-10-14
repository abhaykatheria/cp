# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:46:48 2020

@author: Mithilesh
"""


n,s = map(int,input().split())
coins = list(map(int,input().split()))
coins.sort()
dp = [0 for i in range(s+1)]

for i in range(1,s+1):
    minm = 10**18
    for j in range(len(coins)):
        if i-coins[j]>=0:
            minm = min(minm,dp[i-coins[j]])
        else:
            break
    dp[i] = minm+1
print(dp[s])