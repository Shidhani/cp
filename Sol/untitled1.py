#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 18:02:57 2020

@author: aafaq
"""
file = open("untitled2.txt", "r")

def pal(a):
    if len(a) < 1:
        return "yes"
    
    else:
        if a[0] == a[-1]:
            return pal(a[1:-1])
        else:
            return "No"
    
for line in file:
    
    line = line.strip()
    parts = line.split(" ")
    
    digits = []
    
    n = int(parts[0])
    b = int(parts[1])
    
    if n == 0 and b == 0:
        break
    
    if b != 10:
        
        while n != 0 :
            q = n // b
            r = (n%b) 
            n = q
            digits.append(r)

    else:
         d = str(n)
         for i in range(len(d)):
                 
                 digits.append(int(d[i]))

    print(pal(digits))






 
    
