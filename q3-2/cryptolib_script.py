#from Crypto.Cipher import AES
#from Crypto.Util.Padding import pad
from base64 import b64encode

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

initVector = b'\x00'*16

#Grab Plaintext
#with open('plaintext.txt', 'r') as f:
    #plaintext = f.read()
    #plaintext = plaintext.strip()
plaintext = "This is a top secret."
ptbytes = b'This is a top secret.'
#print(len(ptbytes))
#print(ptbytes)

#Pad the plaintext with all '\x0b's
padded_ptbytes = ptbytes + (16 - (len(plaintext) % 16)) * b'\x0b'
#print(padded_ptbytes)



#Grab ciphertext
#with open('ciphertext.txt', 'r') as f:
#    ciphertext = f.open()
#    ciphertext = ciphertext.strip()

# Convert the hex to bytes, then bytes to a string
#   This string is used to compare with outputted values from dictionary
#   In the final implementation this is redundant but hey I wanted to try it
ciphertext = "8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9"    
ct_hex_bytes = bytes.fromhex(ciphertext)
ctstr = b64encode(ct_hex_bytes).decode('utf-8')



with open('dictionary.txt', 'r') as f:
    finalPad = 10000;
    finalKey = 'FOUND NOTHING'

    #Run through every word in the dictionary
    for line in f:
        #Grab only words less than 16 chars
        currLine = line.strip()
        if (len(currLine) >= 16): continue

        #Pad current word with spaces then grab its bytes
        p_currLine = currLine.ljust(16, ' ')
        p_currLine_bytes = p_currLine.encode('utf-8')

        #Initialize the cipher in CBC mode
        #   Current word in dictionary is the key
        #   Encrypt it using the given word (key) and IV (b'0'*16)
        #   Then, decode the bytes into both a string and into a hexstring
        #   Finally, compare the values in order to find the final key
        cipher = Cipher(algorithms.AES(p_currLine_bytes), modes.CBC(initVector))
        encryptor = cipher.encryptor()
        new_ctbytes = encryptor.update(padded_ptbytes) + encryptor.finalize()

        encstr = b64encode(new_ctbytes).decode('utf-8')
        enchex = new_ctbytes.hex()

        if (ciphertext == enchex) and (ctstr == encstr): 
            print('THERES A MATCH: ' +  currLine + '\n\tHERES THE PADDING: ' + str(11))
            finalKey = currLine

print("\nKey: " + finalKey + '\nPadding: ' + str(11))
