# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 00:18:14 2019

@author: Mithilesh
"""

def bits(a,b):
    a_bin=bin(a)[2:]
    b_bin=bin(b)[2:]
    if(b==(a+1)):
        ans=a&b
    else:
        la,lb=len(a_bin),len(b_bin)
        a_bin='0'*(lb-la)+a_bin
        ans=str(int(a_bin[0])&int(b_bin[0]))
        for i in range(1,lb):
            if(a_bin[i]=='0' or b_bin[i]=='0'):
                ans+='0'
            else:
                if(a_bin[i-1]=='0' and b_bin[i-1]=='0'):
                    ans+='1'
                elif(a_bin[i-1]=='1' and b_bin[i-1]=='1' and ans[i-1]=='1'):
                    ans+='1'
                else:
                    ans+='0'
        ans='0b'+ans
        ans=int(ans,0)
    print(ans)
        

t=int(input())
for q in range(t):
    a,b=map(int,input().split())
    bits(a,b)