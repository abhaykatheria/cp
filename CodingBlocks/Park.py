# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 23:31:28 2019

@author: Mithilesh
"""

def park(n,m,k,s,arr):
    flag=0
    for i in range(n):
        for j in range(m):
            if(arr[i][j]=="*"):
                if s>=0:
                    s+=4
                else:
                    flag=1
                    break
            elif(arr[i][j]=="."):
                if s>=0:
                    s-=3
                else:
                    flag=1
                    break  
            else:
                break
            if(j==m-1):
                s+=1
        if flag==1:
            break
        
    if(s>=k):
        print("Yes")
        print(s)
    else:
        print("No")
    
n,m,k,s=map(int,input().split())
arr=[]
for i in range(n):
    l=list(map(str,input().split()))
    arr.append(l)
park(n,m,k,s,arr)
