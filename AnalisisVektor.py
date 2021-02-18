# -*- coding: utf-8 -*-
"""

@author: Kelompok 11

Modul-modul ini dibuat sebagai tugas proyek akhir mata kuliah Fisika Komputai 1
Susunan anggota kelompok: 
    1. Aldey Wahyu P.		(1606903002)
    2. Daffa Aulia Ekanara	(1606902971)
    3. Fitria Indah Astari	(1606902990)
    4. R. Irfan Ismail		(1606902800)
    5. Nikita Ciamaudi		(1606902813)
    
Vector Operation and Analysis for n-dimensions Vectors Using Python Language (Dot Product, Gradient, Divergence, and Laplacian)
Cross and Curl only gives result for 0, 1, 3, and 7 dimensions
"""

from numpy import array
from sympy import symbols, diff, log, cos, sin, tan, sec, csc, exp, pi

def dotproduct(*v):
    '''
    Memberikan hasil kali dot product antara n-vektor dengan n-dimensi
    Nyatakan vektor dengan list atau tupple (jangan array)
    Apabila terdapat error, coba periksa input (vektor-vektor harus memiliki dimensi yang sama)
    ie:
        a = [1, 2, 3, 4, 5]
        b = [6, 7, 8, 9, 10]
        c = [11, 12, 13, 14]
        dotproduct(a,b,c)
    '''
    x = 0
    if len(v) == 1:
        for i in range(0, len(v[0])):
            x += (v[0][i] * v[0][i])
        return x

    for i in range(0, len(v) - 1):
        if len(v[0]) is not len(v[i]):
            raise Exception("Terdapat vektor dengan jumlah dimensi yang berbeda")
    
    for j in range(0, len(v[0])):
        y = 1
        for k in range(0, len(v)):
            y *= v[k][j]
        x += y

    return x

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

def curl(x,y):
    if len(x) == 0 and len(y) == 0:
        solusi = []
    elif len(x) == 1 and len(y) == 1:
        solusi = [0]
    elif len(x) == 3 and len(y) == 3:
        a = [diff(x[2],y[1])-diff(x[1],y[2]), diff(x[0],y[2])-diff(x[2],y[0]), diff(x[1],y[0])-diff(x[0],y[1])]
        solusi = a
    elif len(x) == 7 and len(y) == 7:
        b = [-diff(x[1],y[2])+diff(x[2],y[1])-diff(x[3],y[4])+diff(x[4],y[3])-diff(x[6],y[5])+diff(x[5],y[6]),
             -diff(x[2],y[0])+diff(x[0],y[2])-diff(x[3],y[5])+diff(x[5],y[3])-diff(x[4],y[6])+diff(x[6],y[4]),
             -diff(x[0],y[1])+diff(x[1],y[0])-diff(x[3],y[6])+diff(x[6],y[3])-diff(x[5],y[4])+diff(x[4],y[5]),
             -diff(x[4],y[0])+diff(x[0],y[4])-diff(x[5],y[1])+diff(x[1],y[5])-diff(x[6],y[2])+diff(x[2],y[6]),
             -diff(x[0],y[3])+diff(x[3],y[0])-diff(x[6],y[1])+diff(x[1],y[6])-diff(x[2],y[5])+diff(x[5],y[2]),
             -diff(x[0],y[6])+diff(x[6],y[0])-diff(x[1],y[3])+diff(x[3],y[1])-diff(x[4],y[2])+diff(x[2],y[4]),
             -diff(x[1],y[4])+diff(x[4],y[1])-diff(x[2],y[3])+diff(x[3],y[2])-diff(x[5],y[0])+diff(x[0],y[5])]
        solusi = b
    else:
        solusi ="Salah satu atau kedua input tidak berdimensi 0, 1, 3, atau 7 Coba periksa input"
    return solusi

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