# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 18:43:20 2018

@author: Mithilesh
"""

def no_of_digit(l,st):
    count,k=0,0
    l=len(st)
    while k<l:
        if st[k].isdigit()==True:
            new_st=st[k+1::]
            while True:
                for i in range(len(new_st)):
                    if new_st[i].isdigit()==False :
                        count+=1
                        st=new_st[i+1::]
                        break
                break
        k+=1
        l=len(st)
    print(count)

    
t=int(input())
for q in range(t):
    l=int(input())
    st=str(input())
    no_of_digit(l,st)