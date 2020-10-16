# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 17:35:38 2018

@author: Mithilesh
"""

def cricket(ov,p):
    score=[0 for x in range(11)]
    st,non_st=1,2
    for i in range(len(ov)):
        if ov[i]=='W':
            st=max(st,non_st)+1
        else:
            temp=int(ov[i])
            if temp%2==0:
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
    for j in range(k,p+1):
        print("Player "+str(k)+": "+"DNB")
        k+=1

t=int(input())
for q in range(t):
    n,p=map(int,input().split())
    ov=input()
    print("Case "+str(q+1)+": ")
    cricket(ov,p)