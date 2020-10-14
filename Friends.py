# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 17:38:02 2020

@author: Mithilesh
"""

dp = [0 for i in range(31)]
dp[1],dp[0]=1,1
for i in range(2,31):
    dp[i] = dp[i-1] + (i-1)*dp[i-2]

for _ in range(int(input())):
    n = int(input())
    print(dp[n])