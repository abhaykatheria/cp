# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 19:12:03 2018

@author: Mithilesh
"""

def hackerearth(l,st):
    arr2=[]
    st2="hackerearth"
    flag=1
    for ch in st2:
        if ch in st:
            if ch=="a" or ch=="e" or ch=="h" or ch=="r":
                arr2.append((st.count(ch))//2)
            else:
                arr2.append(st.count(ch))
        else:
            flag=0
            break
    if flag==0:
        print(0)
    else:
        print(min(arr2))
        
l=int(input())
st=str(input())
hackerearth(l,st)