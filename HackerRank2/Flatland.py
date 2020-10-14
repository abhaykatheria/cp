# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 01:19:19 2018

@author: Mithilesh
"""
import math
def flatland(n,m,space_stations):
    max_dist=dist=city=sp=space_stations[0]
    while city<n:
        if city in space_stations:
            sp=city
            city+=1
        else:
            if sp<space_stations[m-1]:
                dist=min(city-sp,space_stations[space_stations.index(sp)+1]-city)
                if max_dist<dist:
                    max_dist=dist
            else:
                dist=int(math.fabs(city-sp))
                if max_dist<dist:
                    max_dist=dist
            city+=1
    print(max_dist)

n,m=map(int,input().split())
space_stations=list(map(int,input().split()))
space_stations.sort()
flatland(n,m,space_stations)
                