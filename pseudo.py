# -*- coding: utf-8 -*-
import random
import math
"""
------------------------------
RSA Program Pseudocode/Design
------------------------------

RSA_gen_keys()

Display menu for user type {Public user, Private key owner, exit}
if choice == public user:
    Display menu for action {encrypt msg, validate sig, exit}
    if choice == encrypt msg:
        RSA_encrypt()
    elif choice == validate sig:
        RSA_validate()
    else exit()
    
elif choice == key owner:
    Display menu for action {decrypt msg, sign msg, show keys, gen new keys, exit}
    
    if choice == decrypt msg:
        choose msg and RSA_decrypt()
    elif choice == sign msg:
        choose msg and RSA_sign()
    elif choice == show keys:
        RSA_show_keys()
    elif choice == gen keys:
        RSA_gen_keys()
    else exit()
"""

# Function definition
def gen_pseudo_prime(n1, n2, k):
    p = random.randint(n1, n2)
    pseudo_prime = False
    while not pseudo_prime:
        for i in range(k):
            j = random.randint(2,p)
            if pow(j, p-1, p) > 1:
                p = random.randint(n1,n2)
                break
        pseudo_prime = True
    return p

def is_prime(p):
    if p == 2:
        return True
    else:
        for b in range(2, math.floor(math.sqrt(p))):
            if math.gcd(p, b) > 1:
                return False
            else:
                continue
        return True
    
def RSA_gen_keys(n1, n2, k):# Upper and lower bounds for primes
    # Generate and validate large primes p and q    
    while True:
        p = gen_pseudo_prime(n1, n2, k)
        if is_prime(p):
            break
    while True:
        q = gen_pseudo_prime(n1, n2, k)
        if is_prime(q):
            break
        
    # Calculate n and phi
    n = p * q
    phi = (p-1) * (q-1)
    
    # Find e in ring phi relatively prime to phi
    
    # Find d in ring phi, the multiplicative inverse of e
    
    

"""
def RSA_encrypt():
def RSA_decrypt():
def RSA_sign():
def RSA_validate():
def RSA_show_keys():
"""

    
    



