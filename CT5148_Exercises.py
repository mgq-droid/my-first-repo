# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 06:30:47 2025

@author: Admin
"""

names = ["john", "paul", "george", "ringo"]

for i, x in enumerate(names):
    print(i, x)
    
n = ["john", "paul", "george", "ringo"]
n1 = ["lennon", "mccartney", "harrison", "starr"]
instr = ["guitar", "bass", "guitar", "drums"]

for (x, y, z) in zip(n, n1, instr):
    print(x, y, z)

for i, x in enumerate(zip(n, n1, instr)):
    print(i, x)

for i, (a, b, instr) in enumerate(zip(n, n1, instr)):
    print("%d: %s %s, %s" % (i, a, b, instr))

    
    