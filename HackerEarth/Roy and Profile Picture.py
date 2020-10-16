# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:41:54 2018

@author: Mithilesh
"""

def profile_picture(L,W,H):
    if W<L or H<L:
        print("UPLOAD ANOTHER")
    elif (W>=L and H>=L) and (W==H):
        print("ACCEPTED")
    else:
        print("CROP IT")

L=int(input())
N=int(input())
for i in range(0,N):
    W,H=map(int,input().split())
    profile_picture(L,W,H)