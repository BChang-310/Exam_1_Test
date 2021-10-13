# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:08:08 2021

@author: bchan
"""

import numpy as np
import sys


def to_ascii(a_string):
    
    return np.sum([ord(c) for c in a_string])
  
my_username_seed = to_ascii(sys.argv[1])
np.random.seed(my_username_seed)

f = open("Dumb_Template.ipynb", 'r')

a = f.read()
f.close()

a_number = np.random.randint(20, size=3)


a = a.replace("a21 & a22 & a23", 
              f"{a_number[0]} & {a_number[1]} & {a_number[2]}")

output_file = open('Dumb_Template.ipynb', 'w')
output_file.write(a)
output_file.close()
