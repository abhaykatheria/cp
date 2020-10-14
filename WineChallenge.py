# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 18:21:35 2020

@author: Mithilesh
"""

def maximumProfit(cost,i,j,y,dp):
    if i>j:
        return(0)
    if dp[i][j]!=0:
        return(dp[i][j])
    profit1 = cost[i]*y + maximumProfit(cost,i+1,j,y+1,dp)
    profit2 = cost[j]*y + maximumProfit(cost,i,j-1,y+1,dp)
    dp[i][j] = max(profit1,profit2)
    return(max(profit1,profit2))


n = int(input())
dp = [[0 for i in range(n+1)] for j in range(n+1)]
cost = []
for i in range(n):
    ci = int(input())
    cost.append(ci)
y=1
print(maximumProfit(cost,0,n-1,y,dp))
    