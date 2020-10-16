# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:57:27 2018

@author: Mithilesh
"""

def cricket(ov):
    score=[0 for x in range(11)]
    st,non_st=1,2
    for i in range(len(ov)):
        if ov[i]=='W':
            st=max(st,non_st)+1
            if st>11:
                break
        else:
            temp=int(ov[i])
            if temp%2==0:s
                score[st-1]+=temp
            else:
                score[st-1]+=temp
                st,non_st=non_st,st
        if (i+1)%6==0:
            st,non_st=non_st,st
    k=1
    while (k<=max(st,non_st)):
        if (k==st) or (k==non_st):
            print("Player "+str(k)+": "+str(score[k-1])+"*")
        else:
            print("Player "+str(k)+": "+str(score[k-1]))
        k+=1
    
overs=input()
ov=input()
cricket(ov)