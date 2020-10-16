# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 15:53:34 2018

@author: Mithilesh
"""

def ladder(n):
    for i in range(0,n):
        print("""*   *
*   *
*****""")
    print("""*   *
*   *""")
    
n=int(input())
ladder(n)