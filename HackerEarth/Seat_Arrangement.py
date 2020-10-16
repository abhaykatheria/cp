# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 13:39:52 2018

@author: Mithilesh
"""

def seat_arrangement(n):
    quo=n//12
    rem=n%12
    new_seat= (quo*12 + (13-rem))
    if rem==0:
        print(n-11,end=" ")
    else:
        print(new_seat,end=" ")
    if rem>6:
        rem=rem-6
    if rem in [3,4]:
        print("AS")
    elif rem in [2,5]:
        print("MS")
    else:
        print("WS")
    
t=int(input())
for k in range(0,t):
    n=int(input())
    seat_arrangement(n)    