# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:48:15 2020

@author: Mithilesh
"""

n,m = map(int,input().split())
coins = list(map(int,input().split()))
coins.sort()
dp = [0 for i in range(n+1)]
dp[0]=1
for i in range(len(coins)):
    for j in range(coins[i],n+1):
        dp[j]+=dp[j-coins[i]]
print(dp[n])