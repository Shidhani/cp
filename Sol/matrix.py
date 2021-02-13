#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 19:20:46 2020

@author: aafaq
"""


#l.append(input())
#l.append(input())
#l.append(input())

#d= l.find("1")

for i in range(5):
    s= input()
    g= s.find("1")
    if  g > -1:
        f = abs(i-2) +abs(g-2) 
        
    
print(f)