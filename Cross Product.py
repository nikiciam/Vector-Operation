# -*- coding: utf-8 -*-
"""
Created on Sat May 12 17:16:51 2018

@author: Nikita Ciamaudi
"""

from numpy import array
def crossproduct(x,y):
    """
    Memberikan hasil kali cross product antara dua vektor berdimensi 0, 1, 3, atau 7
    Nyatakan kedua vektor dalam bentuk array 
    [e1, e2, e3, e4, e5, e6, e7]
    dengan en menyatakan dimensi
    Referensi: https://arxiv.org/pdf/1212.3515.pdf
    """
    if len(x) == 0 and len(y) == 0:
        solusi = []
    elif len(x) == 1 and len(y) == 1:
        solusi = array([0])
    elif len(x) == 3 and len(y) == 3:
        a = []
        a.append (x[1]*y[2]-x[2]*y[1])
        a.append (x[2]*y[0]-x[0]*y[2])
        a.append (x[0]*y[1]-x[1]*y[0])
        solusi = a
    elif len(x) == 7 and len(y) == 7:
        b = []
        b.append (-x[2]*y[1]+x[1]*y[2]-x[4]*y[3]+x[3]*y[4]-x[5]*y[6]+x[6]*y[5])
        b.append (-x[0]*y[2]+x[2]*y[0]-x[5]*y[3]+x[3]*y[5]-x[6]*y[4]+x[4]*y[6])
        b.append (-x[1]*y[0]+x[0]*y[1]-x[6]*y[3]+x[3]*y[6]-x[4]*y[5]+x[5]*y[4])
        b.append (-x[0]*y[4]+x[4]*y[0]-x[1]*y[5]+x[5]*y[1]-x[2]*y[6]+x[6]*y[2])
        b.append (-x[3]*y[0]+x[0]*y[3]-x[1]*y[6]+x[6]*y[1]-x[5]*y[2]+x[2]*y[5])
        b.append (-x[6]*y[0]+x[0]*y[6]-x[3]*y[1]+x[1]*y[3]-x[2]*y[4]+x[4]*y[2])
        b.append (-x[4]*y[1]+x[1]*y[4]-x[3]*y[2]+x[2]*y[3]-x[0]*y[5]+x[5]*y[0])
        solusi = b
    else:
        solusi ="Salah satu atau kedua input tidak berdimensi 0, 1, 3, atau 7 Coba periksa input"
    return solusi