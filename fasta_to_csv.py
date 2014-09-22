# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 17:58:22 2014

@author: MJMV
"""

## file containing sequences in csv format
## change path to desired file
f = open("C:/Users/", "r")

## output file to contain extracted sequences
## change name to desired name/location
o = open("C:/Users/", "w")

for line in f:
    if ">" in line:
        title = line.replace("\n", ",")
        
 ## unhash line below if want ">" removed from sequence title
        
 #       title2 = title.replace(">", "")  
        
    else:
        sequence = line

    o.write(title + sequence)
    
## hash line above and unhash line below if ">" is removed from sequence title
    
    #o.write(title2 + sequence)
    
o.close()

    
