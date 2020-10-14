# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 12:16:10 2019

@author: Mithilesh
"""

def pallin_index(string):
    if string==string[-1::-1]:
        return(-1)
    else:
        arr=[0 for i in range(26)]
        for ch in string:
            arr[ord(ch)-97]+=1
        for ch2 in arr:
            if(ch2==1):
                return(string.index(ch2))

t=int(input())
for i in range(t):    
    string=str(input())
    print(pallin_index(string))