# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 17:52:24 2018

@author: Mithilesh
"""

def sherlock(st):
    Months=['January','February','March','April','May','June','July','August','September','October','November','December']
    if st[0].isdigit()==True:
        if st[1].isdigit()==True:
            date=int(st[:2])
        else:
            date=int(st[0])
        print(date)
    for ch in Months:
        if ch in st:
            month=ch
            ind=Months.index(ch)print(ch,ind)
    year=int(st[-4::])
    
    if date==1:
        if ind in [0,1,3,5,7,8,10]:
            month=Months[ind-1]
            date=31
            if ind==0:
                year-=1
        elif ind in [4,6,9,11]:
            month=Months[ind-1]
            date=30
        else:
            month=Months[ind-1]
            if year%100==0 and year%400==0:
                date=29
            elif year%4==0 and year%100!=0:
                date=29
            elif year%100==0 and year%400!=0:
                date=28
            else:
                date=28
    else:
        date-=1
    print(str(date)+" "+str(month)+" "+str(year))

t=int(input())
for q in range(t):
    st=str(input())
    sherlock(st)