# -*- coding: utf-8 -*-
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
    
def RSA_gen_keys()
def RSA_encrypt()
def RSA_decrypt()
def RSA_sign()
def RSA_validate()
def RSA_show_keys()

    
    

"""

