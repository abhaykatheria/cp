# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 16:08:28 2018

@author: Mithilesh
"""

def cipher(message,k):
    new_message=""
    z=k%26
    d=k%10
    for ch in message:
        if ch.isupper()==True:
            var=ord(ch)+z
            if var>90:
                var=64+(var-90)
            new_message+=chr(var)
        elif ch.islower()==True:
            var=ord(ch)+z
            if var>122:
                var=96+(var-122)
            new_message+=chr(var)
        elif ch.isdigit()==True:
            if (int(ch)+d)<10:
                new_message+=str(int(ch)+d)
            else:
                new_message+=str(int(ch)+d-10)
        else:
            new_message+=ch
    print(new_message)

message=input()
k=int(input())
cipher(message,k)