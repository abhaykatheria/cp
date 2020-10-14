# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 19:29:50 2020

@author: Mithilesh
"""

for _ in range(int(input())):
    n,m = map(int,input().split())
    dp = [0]*(n+1)
    for i in range(n+1):
        if i<m:
            dp[i]=1
        elif i==m:
            dp[i]=2
        else:
            dp[i] = dp[i-1]+dp[i-m]
    print(dp[n])