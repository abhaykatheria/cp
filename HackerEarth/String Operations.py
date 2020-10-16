# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 02:15:02 2018

@author: Mithilesh
"""

s=str(input())
q=int(input())
for i in range(q):
    ind,ch=map(str,input().split())
    s=s[:int(ind)-1]+ch+s[int(ind):]
stri,count=str(s),0
m=int(input())
for j in range(m):
    a,b=map(int,input().split())
    temp=s[a-1:b]
    temp=temp[-1::-1]
    s=s[:a-1]+temp+s[b:]
fri=s
for k in range(len(s)):
    if stri[k]==fri[k]:
        count+=1
        
print(stri)
print(fri)
print(count)