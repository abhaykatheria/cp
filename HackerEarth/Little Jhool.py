# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 19:36:13 2018

@author: Mithilesh
"""

def little_jhool(n):
    count=0
    n=list(str(n))
    k=n[0]
    for ch in n:
        if ch==k:
            count+=1
            print(count,k)
            if count==6:
                print("Sorry, sorry!")
                break
        else:
            count=1
            if n[0]=='1':
                k='0'
            else:
                k='1'
            print(k)
    if count<6:
        print("Good Luck!")
    
n=input()
little_jhool(n)