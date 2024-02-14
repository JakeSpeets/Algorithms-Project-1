"""
Algorithms Project 1
Eric Merideth - Jacob Speights - Michael Olaoye

 - This is the main driver file for our RSA cryptosystem.
 - The main() function makes calls to the other three files imported below.

"""

import e_d_crypt
import keyGen
import d_sig

def main():
    '''Main driver'''
    # Generate RSA keys, store in local variables
    keyList = keyGen.RSA_gen_keys(10000, 100000)  # Prime number range: 10,000 to 100,000
    print('RSA keys have been generated.')

    # List return order: (p, q, n, e, d, phi)
    keys_p = keyList[0]
    keys_q = keyList[1]
    keys_n = keyList[2]
    keys_e = keyList[3]
    keys_d = keyList[4]
    keys_phi = keyList[5]
    
    
    plain_msg = []
    msg_sig = []
    enc_msg = []


    prog_exit = False
    while (prog_exit == False):
        
        # User type selection
        print ('Please select your user type:')
        print ('\t1. A public user')
        print ('\t2. The owner of the keys')
        print ('\t3. Exit program')
        u_sel = input("\nEnter your choice: ")

        # A public user
        if (u_sel == '1'):
            pub = True

            while (pub == True):
                # List of options for a public user
                print ('\nAs a public user, what would you like to do?')
                print ('\t1. Send an encrypted message')
                print ('\t2. Authenticate a digital signature')
                print ('\t3. Exit')
                p_sel = input("\nEnter your choice: ")

                # Send an encrypted message
                if (p_sel == '1'):
                    message = input('\nEnter a message: ')
                    enc_msg.append(e_d_crypt.encrypt_string(message, keys_e, keys_n))
                    print ('Message encrypted and sent.')

                # Authenticate digital signature
                elif (p_sel == '2'):
                    if not msg_sig: # If no signatures in the signature array
                        print ('There are no signatures to authenticate')

                    else: # If there are signatures to be read
                        auth_exit = False
                        a_choices = [] 
                        while (auth_exit == False):

                            # Displays all available signatures
                            print('\nThe following messages are available:')
                            a_choices = []
                            for i, sig in enumerate(plain_msg, start=1):
                                print(f"{i}. {sig}")
                                a_choices.append(i)

                            # Prompts for choice
                            a_sel = int(input("\nEnter your choice: "))                            
                            if 0 < a_sel <= len(plain_msg):  # Check if the choice was a valid number
                                test_sig = msg_sig[a_sel - 1]
                                txt_sig = plain_msg[a_sel - 1]
                                if d_sig.authenticate(test_sig, keys_n, keys_e) == txt_sig:
                                    validity = "valid." 
                                else: validity = "invalid."
                                print("Signature is", validity)
                            else: print("Invalid Selection")
                            auth_exit = True

                # Return to main menu
                elif (p_sel == '3'):
                    k_own = True
                    print ('\n')
                    prog_exit = False
                    break

        # User selects owner
        elif (u_sel == '2'):
            k_own = True

            # List of options for the key owner
            while (k_own == True):
                print ('\nAs the owner of the keys, what would you like to do?')
                print ('\t1. Decrypt a received message')
                print ('\t2. Digitally sign a message')
                print ('\t3. Show the keys')
                print ('\t4. Generate a new set of keys')
                print ('\t5. Exit')
                o_sel = input("\nEnter your choice: ")

                # Decrypt a received message
                if (o_sel == '1'):
                    if not enc_msg: # If no messages in the encrypted messages array
                        print ('There are no messages to decrypt')

                    else:
                        # Input validation
                        decrypt_exit = False
                        decrypt_choices = []
                        while (decrypt_exit == False):

                            print('\nThe following messages are available:')
                            decrypt_choices = []
                            for i in range(len(enc_msg)):
                                print(f"{i + 1}. (Length = {len(enc_msg[i])})")
                                decrypt_choices.append(i + 1)
                            
                            decrypt_choice = int(input("\nEnter your choice: "))
                            
                            if 0 < decrypt_choice <= len(enc_msg):
                                decrypted_message = e_d_crypt.decrypt_string(enc_msg[decrypt_choice - 1], keys_d, keys_n)
                                crypt_valid = True
                                for i in range(len(decrypted_message)): # ASCII code validation
                                    if not (0 <= decrypted_message[i] < 256):
                                        crypt_valid = False
                                        break
                                if crypt_valid:
                                    str = bytes(decrypted_message).decode('ascii')
                                    print('Decrypted message:', str)
                                else: print("Could not decrypt this message!")
                            else: print("Invalid Selection")
                            decrypt_exit = True # Exits menu

                # Sign a message
                elif (o_sel == '2'):
                    msg = input('\nEnter a message: ')
                    plain_msg.append(msg) # stores signature text in list
                    msg_sig.append(d_sig.sign(msg, keys_n, keys_d)) # signs the message and stores in array

                    print ('Message signed and sent.')

                # Displays RSA keys and other values
                elif (o_sel == '3'):
                    print("p:", keys_p)
                    print("q:", keys_q)
                    print("n:", keys_n)
                    print("e:", keys_e)
                    print("d:", keys_d)
                    print("phi:", keys_phi)
                    
                elif (o_sel == '4'):
                    # Generate RSA keys, store in local variables
                    keyList = keyGen.RSA_gen_keys(10000, 100000)  # Prime number range: 10,000 to 100,000
                    print('New RSA keys have been generated.')

                    # List return order: (p, q, n, e, d, phi)
                    keys_p = keyList[0]
                    keys_q = keyList[1]
                    keys_n = keyList[2]
                    keys_e = keyList[3]
                    keys_d = keyList[4]
                    keys_phi = keyList[5]

                # Return to main menu
                elif (o_sel == '5'):
                    k_own = False
                    print ('\n')

        # Exit program
        elif (u_sel == '3'):
            prog_exit = True

        else: # Input validation
            print('\nPlease enter a valid choice (1-3).\n')

    print ('\nExiting...')

main()