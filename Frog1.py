# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 18:47:59 2020

@author: Mithilesh
"""

n = int(input())
arr = list(map(int,input().split()))
dp = [0]*n

dp[1] = abs(arr[1]-arr[0])

for i in range(2,n):
    op1 = dp[i-2] + abs(arr[i]-arr[i-2])
    op2 = dp[i-1] + abs(arr[i]-arr[i-1])
    dp[i] = min(op1,op2)

print(dp[-1])