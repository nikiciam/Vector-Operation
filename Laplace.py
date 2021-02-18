# -*- coding: utf-8 -*-
"""
Created on Tue May 15 00:13:22 2018

@author: Nikita Ciamaudi
"""

from sympy import *

def laplace (f,x):
    """
    Memberikan output berupa laplace fungsi n-variabel 
    Nyatakan f sebagai suatu vektor dengan list 
    Nyatakan x sebagai dimensi yang dimaksud dengan list
    Urutan f dan x memengaruhi solusi
    Jangan lupa mendefinisikan symbol dengan sympy
    ie :
        f = [-25**(e1/e3) + 76**(e1**(e4*e5)) + 89*e3**e2 + (85*e1)**e2 + 32/e2]
        x = [e1, e2, e3, e4, e5]
    """
    a = tuple(fi.diff(xi) for fi, xi in zip((len(x)*f), x))
    return sum(ai.diff(xi) for ai, xi in zip(a, x))