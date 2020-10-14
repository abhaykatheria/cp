# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 15:53:09 2018

@author: Mithilesh
"""

def making_anagrams(str1,str2):
    lst1=list(str1)
    lst2=list(str2)
    lst3,lst4=list(lst1),list(lst2)
    l1,l2=len(str1),len(str2)
    if str1==str2 or str1[::]==str2[-1::-1]:
        print(0)
    elif l1<l2:
        for i in range(0,l1):
            if lst3[i] in lst2:
                lst1.remove(lst3[i])
                lst2.remove(lst3[i])
        print(len(lst1)+len(lst2))
    else:
        for i in range(0,l2):
            if lst4[i] in lst1:
                lst2.remove(lst4[i])
                lst1.remove(lst4[i])
        print(len(lst1)+len(lst2))
    
n=int(input())
for z in range(0,n):
    str1=str(input("Enter the string1: "))
    str2=str(input("Enter the string2: "))
    making_anagrams(str1,str2)
            
    