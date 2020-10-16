# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 23:40:47 2019

@author: Mithilesh
"""

def frequency(string):
    count=1
    for i in range(1,len(string)):
        if(string[i]!=string[i-1]):
            print(string[i-1]+str(count),end="")
            count=1
        else:
            count+=1
    print(string[-1]+str(count),end="")
string=input()
frequency(string)