# -*- coding: utf-8 -*-
"""
Created on Mon May 14 23:14:01 2018

@author: Nikita Ciamaudi
"""

from sympy import *

def gradient (f, x):
    """
    Memberikan output berupa gradient fungsi n-variabel (dinyatakan dengan vektor n-dimensi) 
    Nyatakan f sebagai suatu fungsi dengan list 
    Nyatakan x sebagai dimensi yang dimaksud dengan list
    Urutan f dan x memengaruhi solusi
    Jangan lupa mendefinisikan symbol dengan sympy
    ie :
        f = [-25**(e1/e3) + 76**(e1**(e4*e5)) + 89*e3**e2 + (85*e1)**e2 + 32/e2]
        x = [e1, e2, e3, e4, e5]
    """
    return tuple(fi.diff(xi) for fi, xi in zip((len(x)*f), x))