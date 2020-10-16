# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 13:42:24 2018

@author: Mithilesh
"""

def alice_bob(n,alice,bob):
    sum_a,sum_b=0,0
    for i in range(n):
        sum_a+=alice[i]
        sum_b+=bob[i]
    if sum_a>sum_b:
        print("Alice")
    elif sum_a<sum_b:
        print("Bob")
    else:
        print("Tie")
    
t=int(input())
for q in range(t):
    n=int(input())
    bob=list(map(int,input().split()))
    alice=list(map(int,input().split()))
    alice_bob(n,alice,bob)