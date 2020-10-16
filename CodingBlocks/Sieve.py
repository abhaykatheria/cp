# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:44:11 2019

@author: Mithilesh
"""

def seive(n=10000000):
    prime=[0 for i in range(n+1)]
    prime[0]=prime[1]=0
    prime[2]=1
    for i in range(3,n+1,2):
        prime[i]=1
    for i in range(3,n+1,2):
        if prime[i]==1:
            for j in range(i*i,n+1,2*i):
                prime[j]=0
    new_prime=[0]
    for k in range(n+1):
        if prime[k]==1:
            new_prime.append(k)
    return(new_prime)

k=int(input())
prime=seive()
print(prime[k])