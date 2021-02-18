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
