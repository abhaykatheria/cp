# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 22:03:50 2018

@author: Mithilesh
"""

def quad(a,b,c):
    root_1,root_2=0,0
    dis=(b*b)-(4*a*c)
    if dis>=0:
        root_1= int(((-b)+dis**0.5)/(2*a))
        root_2= int(((-b)-dis**0.5)/(2*a))
        if dis==0:
            print("Real and Equal")
            print(root_1,root_2)
        else:
            print("Real and Distinct")
            print(root_1,root_2)
    else:
        print("Imaginary")

a,b,c=map(int,input().split())
quad(a,b,c)