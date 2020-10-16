# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 23:23:58 2018

@author: Mithilesh
"""

def pyschic(n,arr,s,e):
    temp=arr[s-1]
    arb=0
    if s==e:
        print("Yes")
    elif s==arr[s-1]:
        print("No")
    else:
        while True:
          if temp!=e:
              temp=arr[temp-1]
              arb+=1
          elif temp==arr[s-1] and arb!=0:
              arb+=1
              print("No")
              break
          else:
              print("Yes")
              break

n=int(input())
arr=list(map(int,input().split()))
s,e=map(int,input().split())
pyschic(n,arr,s,e)