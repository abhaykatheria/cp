# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:56:20 2019

@author: Mithilesh
"""

def pallin(string):
    arr=[0 for i in range(26)]
    for ch in string:
        arr[ord(ch)-97]+=1
    odd_val=0
    for ch2 in arr:
        if(ch2%2!=0):
            odd_val+=1
        if odd_val>1:
            return(False)
    return(True)
    
string=str(input())
if (pallin(string)):
    print("YES")
else:
    print("NO")
    
        