# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 23:20:27 2019

@author: Mithilesh
"""
def prnt(mat):
    for ch in mat:
        for ch2 in ch:
            print(ch2,end="")
        print()

def cavity(mat,n):
    if n==2:
        prnt(mat)
    else:
        mat2=[x[:] for x in mat]
        for i in range(1,n-1):
            for j in range(1,n-1):
                if mat[i][j]>mat[i][j-1] and mat[i][j]>mat[i][j+1] and mat[i][j]>mat[i+1][j] and mat[i][j]>mat[i-1][j]:
                        mat2[i][j]="X"
        prnt(mat2)
    
n=int(input())
mat=[]
for r in range(n):
    rows=str(input())
    rows=list(map(int,str(rows)))
    mat.append(rows)   
cavity(mat,n)