# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 13:53:24 2018

@author: Mithilesh
"""

try:
  arr=[]
  while True:
    n=int(input())
    arr.append(n)
except ValueError:
    sum1=0
    for ch in arr:
      sum1+=ch
      if sum1>=0:
        print(ch)
      else:
        break