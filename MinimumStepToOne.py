# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 22:02:52 2020

@author: Mithilesh
"""

dp = [0 for i in range(1000001)]
dp[1]=0
dp[2]=1
for i in range(3,1000001):
    x,y = 10**18,10**18
    if i%3==0:
        x=dp[i//3]
    if i%2==0:
        y=dp[i//2]
    dp[i] = min(x,y,dp[i-1])+1
    
for i in range(int(input())):
    n = int(input())
    print("Case "+str(i+1)+": "+str(dp[n]))