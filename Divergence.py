# -*- coding: utf-8 -*-
"""
Created on Sun May 13 10:49:36 2018

@author: Nikita Ciamaudi
"""

from sympy import *
def divergence(f, x):
    """
    Memberikan output berupa divergensi vektor n-dimensi
    Nyatakan f sebagai suatu vektor dengan list 
    Nyatakan x sebagai dimensi yang dimaksud dengan list
    Urutan f dan x memengaruhi solusi
    Jangan lupa mendefinisikan symbol dengan sympy
    ie :
        f = [x*y, x**y, 2**z]
        x = [x, y, z]
    """
    return sum(fi.diff(xi) for fi, xi in zip(f, x))