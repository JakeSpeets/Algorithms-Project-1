"""
Algorithms Project 1
Eric Merideth - Jacob Speights - Michael Olaoye

This file handles all encryption/decryption functions,
as well as any helper functions needed.
"""

def encrypt_recursive(m, e, n):
    ''' Evaluates m^e mod n, returns c '''
    if e == 0:
        return 1
    if e % 2 == 0:
        t = encrypt_recursive(m, e//2, n)
        return (t*t) % n
    else:
        t = encrypt_recursive(m, e//2, n)
        return m * (t**2 % n) % n

def decrypt_recursive(c, d, n):
    ''' Evaluates c^d mod n, returns m '''
    if d == 0:
        return 1
    if d % 2 == 0:
        t = decrypt_recursive(c, d // 2, n)
        return (t * t) % n
    else:
        t = decrypt_recursive(c, d // 2, n)
        return c * (t ** 2 % n) % n


# Takes a string and converts the characters to ascii values, then sends each of those values to the encryption method
def encrypt_string(str, e, n):
    '''Processes and encrypts a string'''
    string = list(str.encode('ascii'))
    encrypt = list()
    for i in string:
        encrypt.append(encrypt_recursive(i, e, n))
    return encrypt


# Runs encrypted ascii values and decrypts them with the private key
def decrypt_string(c, d, n):
    '''Processes and decrypts a string'''
    decrypt = list()
    for i in c:
        decrypt.append(decrypt_recursive(i, d, n))
    return decrypt
