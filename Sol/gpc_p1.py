#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 09:48:42 2020

@author: aafaq
"""

file = open("purifier.txt", "r")

cases = int(file.readline().strip())
i= 0


print(cases)

            
while i < cases:
    
    line = file.readline()
    
    line = line.split()       
    x = int(line[0])
    y = int(line[1])
     
    busy = 0
        
    
    z = 0
    while z < y:
             
            times = file.readline()
            
            times = times.strip("\n")
            blocks = times.count(" ")
            times = times.replace(":", " ")
            times = times.replace("-", " ")
            times = times.split()
            print(times)
            z+= 1
            l = 0
            while l != len(times) :
                 if len(times) != "" :
                     hours = abs(int(times[l+2]) - int(times[l]))
                     hours = hours * 60
                     
                     minutes = abs(int(times[l+3]) - int(times[l+1]))
                     
                     busy+= hours + minutes
                     l = l +4   
                 else:
                     busy+= 14*60
                     l = l +4                        
     
    if ((14*60*y) - busy) >= (x*60):
       print("Yes")  

    else:
       print("No")
       
       
    i = i +1


  