# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 00:26:56 2018

@author: Mithilesh
"""

def pallindromic_cipher(st):
    pdt=1
    if st==st[-1::-1]:
        print("Pallindrome")
    else:
        for ch in st:
            pdt*=(ord(ch)-96)
        print(pdt)

t=int(input())
for q in range(t):
    st=input()
    pallindromic_cipher(st)