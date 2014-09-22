# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 19:22:06 2014

@author: MJMV
"""


## file containing sequences in csv format
## change path to desired file
f = open('C:/Users/', 'r') 

## file containing identifier for sequences to extract (names, motifs, etc.) 
## file contains each identifier on a separate line
## change path to desired file
r = open('C:/Users/', 'r') 

## output file to contain extracted sequences
## change name to desired name/location
o= open('C:/Users/', 'w') 


taxa = []
entries = []

for entry in f:
    if entry not in entries:
        entries.append(entry)

for taxon in r:
    taxon2 = taxon.rstrip("\n")
    if taxon2 not in taxa:
        taxa.append(taxon2)
      
for taxon in taxa:
    for entry in entries:
        if taxon in entry:
            o.write(entry)

o.close()
      
   
