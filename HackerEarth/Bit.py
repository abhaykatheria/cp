# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:09:31 2018

@author: Mithilesh
"""
try:
    while True:
        n=int(input())
        d=bin(n)
        d=str(d)
        co=d.count('1')
        print(co)
except IOError:
    print("")

    