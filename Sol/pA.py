#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:36:09 2020

@author: aafaq
"""
l = int(input())
c=0
for i in range(l):
    g=0
    m = list(map(int, input().split()))
#    for f in range(m):
#        g+= f
    if sum(m) >= 2:
        c+=1
    
print(c)
    
    
