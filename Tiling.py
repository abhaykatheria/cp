# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 17:20:31 2020

@author: Mithilesh
"""
   
n =int(input())
dp = [0]*(n+1)

for i in range(n+1):
    if i<=3:
        dp[i]=1
    elif i==4:
        dp[i]=2
    else:
        dp[i] = dp[i-1]+dp[i-4]
    
print(dp[n])