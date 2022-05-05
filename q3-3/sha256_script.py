from cryptography.hazmat.primitives import hashes
from base64 import b64encode
from random import seed, randbytes


#First, generate some random bytes
#   This is hashed and used as the initial hash
random.seed()
randbytes = random.randbytes(16) 

digest = hashes.Hash(hashes.SHA256())

print(randbytes)

digest.update(randbytes)
hashbytes = digest.finalize()

s_hashbytes = hashbytes[:3]

s_hashhex = s_hashbytes.hex()
#hashhex = hashbytes.hex()

s_hashstr = b64encode(s_hashbytes).decode('utf-8')
#hashstr = b64encode(hashbytes).decode('utf-8')

print(hashbytes)
print(s_hashbytes)
print(s_hashhex)
print(s_hashstr)

counter = 0


#WEAK COLLISION TESTING

while 1 == 1:
    digest = hashes.Hash(hashes.SHA256())
    ctr_bytes = str(counter).encode('UTF-8')

    digest.update(ctr_bytes)
    new_hashbytes = digest.finalize()
    new_s_hashbytes = new_hashbytes[:3]

    new_s_hashhex = new_s_hashbytes.hex()

    #Since we're comparing the hexes, cut off every 2 values (i.e. 2 hex nums, or 1 byte)
    #if (s_hashhex[:2] == new_s_hashhex[:2]):
        #print("1 Byte Collision Found at cycle: " + str(counter) +  "\n\tOld Hash: " + s_hashhex + "; New Hash: " + new_s_hashhex)

    if (s_hashhex[:4] == new_s_hashhex[:4]):
        print("2 Byte Collision Found at cycle: " + str(counter) +  "\n\tOld Hash: " + s_hashhex + "; New Hash: " + new_s_hashhex)

    if (s_hashhex == new_s_hashhex):
        print("Full Collision Found at cycle: " + str(counter) +  "\n\tOld Hash: " + s_hashhex + "; New Hash: " + new_s_hashhex)
        break

    counter+=1 
