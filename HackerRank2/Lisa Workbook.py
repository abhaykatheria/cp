# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 21:48:46 2018

@author: Mithilesh
"""

def lisa_workbook(l,p,ch_arr):   #p for problems per page
    special_ques,pageNumber=0,0
    for i in range(l):
        problem=1
        pageNumber+=1
        while ch_arr[i]!=0:
            if (problem==pageNumber):
                special_ques+=1
            if(problem%p==0 and ch_arr[i]!=0):
                pageNumber+=1
            ch_arr[i]-=1
            problem+=1
        if (problem-1)%p==0:
            pageNumber-=1
        print(special_ques)
    
l,p=map(int,input().split())
ch_arr=list(map(int,input().split()))
lisa_workbook(l,p,ch_arr)