from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode

initVector = b'\x00'*16
finalKey = "Found Nothing (default outcome)"

#Grab Plaintext
with open('plaintext.txt', 'r') as f:
    #plaintext = f.read()
    #plaintext = plaintext.strip()
    plaintext = "This is a top secret."
    ptbytes = b'This is a top secret.'
    print(len(ptbytes))
    #ptbytes = plaintext.encode('utf-8')
    print(ptbytes)
    #Pad the plaintext with all 0s
    padded_ptbytes = ptbytes + (AES.block_size - (len(plaintext) % AES.block_size)) * b'\x11'
    print(padded_ptbytes)

#Grab ciphertext
#   Convert the hex to bytes, then bytes to a string
#   This string is used to compare with outputted values from dictionary
with open('ciphertext.txt', 'r') as f:
    #ciphertext = f.read()
    #ciphertext = ciphertext.strip()
    ciphertext = "8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9"
    
    ct_hex_bytes = bytes.fromhex(ciphertext)
    ctstr = b64encode(ct_hex_bytes).decode('utf-8')
    print(ciphertext)
    print(ctstr)

finalPad = 1000

with open('dictionary.txt', 'r') as f:
    #Run through every word in the dictionary
    for line in f:
        #Grab only words less than 16 chars
        currLine = line.strip()
        if (len(currLine) >= 16): continue

        #Pad current word with spaces
        p_currLine = currLine.ljust(16, ' ')
        #p_currLine = "{:<16}".format(currLine)
        p_currLine_bytes = p_currLine.encode('utf-8')

        #Initialize the cipher in CBC mode
        #   Current word in dictionary is the key
        #   Encrypt it using the given word (key) and IV (b'\x00'*16)
        #   Then, decode the bytes and the new encrypted string is found
        cipher = AES.new(p_currLine_bytes, AES.MODE_CBC, initVector)

        new_ctbytes = cipher.encrypt(padded_ptbytes)
        encstr = b64encode(new_ctbytes).decode('utf-8')
        enchex = new_ctbytes.hex()


        if (ciphertext == enchex) or (ctstr == encstr):
            finalDict = currLine
            finalPad = i

print("\n" + finalKey + '\tPadding: ' + str(finalPad))
print("Tried to match: " + ciphertext)
print("Tried to match: " + ctstr)
