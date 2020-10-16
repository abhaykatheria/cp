# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 22:59:52 2019

@author: Mithilesh
"""

def duration(sh,sm,eh,em):
    dur_H=0
    dur_M=0
    if sm>em:
        dur_H=eh-sh-1
        dur_M=em+60-sm
    elif sm<=em:
        dur_H=eh-sh
        dur_M=em-sm
    print(dur_H,dur_M)
    
t=int(input())
for i in range(t):
    sh,sm,eh,em=map(int,input().split())
    duration(sh,sm,eh,em)