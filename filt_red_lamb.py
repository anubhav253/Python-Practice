# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 13:58:46 2018

@author: DEVIL
"""

def f(x): return x % 3 == 0 or x % 5 == 0
filter(f, range(2,25))



def cube(x): return x*x*x
map(cube, range(1,11))



def add(x, y): return x+y
reduce(add, range(1,11))



filter(lambda x: x % 3 ==0, range(1,11))


map(lambda x: x * 3 + 10, range(1,11))


reduce(lambda x,y: x + y, range(1,11))