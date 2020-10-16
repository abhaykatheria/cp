# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 01:55:22 2019

@author: Mithilesh
"""

def compute(s):
    l=len(s)
    frst_part=2*(2**(l-1)-1)
    scnd_part=0
    s=s[-1::-1]
    for i in range(l):
        if(s[i]=='4'):
            continue
        else:
            scnd_part+=2**i
    print(frst_part+scnd_part+1)
    
s=input()
compute(s)