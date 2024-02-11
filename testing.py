# -*- coding: utf-8 -*-
"""
Testing
"""

import keyGen

keys = keyGen.RSA_gen_keys(pow(10, 10), pow(10,12))
# Key list format (p, q, n, e, d, phi)

p = keys[0]
q = keys[1]
n = keys[2]
e = keys[3]
d = keys[4]
phi = keys[5]

print("p-value: ", p)
print("q-value: ", q)
print("n-value: ", n)
print("e-value: ", e)
print("d-value: ", d)
print("phi-value: ", phi)
