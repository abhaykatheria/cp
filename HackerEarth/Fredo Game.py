# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 12:56:34 2018

@author: Mithilesh
"""

def fredo_game(ammo,n,arr):
    flag=0
    for i in range(n):
        if arr[i]==0:
            ammo-=1
        elif arr[i]==1:
            ammo+=2
        if ammo==0:
            flag=i+1
            break
    if flag==0:
        print("Yes",ammo)
    else:
        if flag==n:
           print("Yes",ammo)
        else:
            print("No",flag)
t=int(input())
for q in range(t):
    ammo,n=map(int,input().split())
    arr=list(map(int,input().split()))
    fredo_game(ammo,n,arr)
        