"""
Algorithms Project 1
Eric Merideth - Jacob Speights - Michael Olaoye

This file handles the signing and authenticating
of digital signatures.
"""

def fastExpo_rec (c, d, n): # sourced from Dr. Hu's slides
    if d == 0:
        return 1
    if d%2 == 0:
        t = fastExpo_rec (c, d//2, n)
        return (t*t)%n
    else:
        t = fastExpo_rec (c, d//2, n)
        return c *(t**2%n)%n

def sign(m, n, d):
    '''Creates a digital signature'''
    intList = list(m.encode('ascii')) # converts to ASCII codes
    s = list()
    for i in intList:
        s.append(fastExpo_rec(i, d, n))
    return s

def authenticate(s, n, e):
    '''Authenticates a digital signature'''
    m = list()
    for i in s:
        m.append(fastExpo_rec(i, e, n))
    crypt_valid = True
    for i in range(len(m)): # ASCII code validation
        if not (0 <= m[i] < 256):
            crypt_valid = False
            break
    if crypt_valid:
        str = bytes(m).decode('ascii')
        return str
    else: print("Could not authenticate this message!")
    