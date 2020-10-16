# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 22:17:07 2018

@author: Mithilesh
"""

def ali(st):
    st=list(st)
    char=st.pop(2)
    st.remove('-')
    count=0
    if char in ['A','E','I','O','U']:
        flag=0
    else:
        for i in range(0,len(st)-1):
            sum1=int(st[i])+int(st[i+1])
            if sum1%2==0:
                count+=1
                sum1=0
            else:
                flag=0
                break
    if flag==0:
        print("invalid")
    elif count==5 and flag!=0:
        print("valid")
        
st=input()
ali(st)