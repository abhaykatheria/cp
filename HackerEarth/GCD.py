# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 21:19:31 2018

@author: Mithilesh
"""

def gcd(n1,n2):
    gd,b,a=1,min(n1,n2),max(n1,n2)
    for i in range(1,int(b**0.5)+1):
        if b%i==0:
            if a%i==0 and a%(b//i)==0:
                gd=b//i
                break
            elif a%i!=0 and a%(b//i)==0:
                gd=b//i
                break
            elif a%i==0 and a%(b//i)!=0:
                gd=i
        else:
            continue
    return(gd)

def lcm(n1,n2):
    lcm=(n1*n2)//gcd(n1,n2)
    return(lcm)
n1,n2=map(int,input("Enter two numbers whose gcd & lcm you want to know: ").split())
gc=gcd(n1,n2)
lc=lcm(n1,n2)
print("GCD is : ",gc)
print("LCM is : ",lc)