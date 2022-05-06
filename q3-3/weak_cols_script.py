from cryptography.hazmat.primitives import hashes
from base64 import b64encode
import random

#First, generate some random bytes
#   This is hashed and used as the initial hash
random.seed()
randbytes = random.randbytes(16) 

digest = hashes.Hash(hashes.SHA256())

#print(randbytes)

digest.update(randbytes)
hashbytes = digest.finalize()

s_hashbytes = hashbytes[:3]

s_hashhex = s_hashbytes.hex()
#hashhex = hashbytes.hex()

#s_hashstr = b64encode(s_hashbytes).decode('utf-8')
#hashstr = b64encode(hashbytes).decode('utf-8')

print(hashbytes)
print(s_hashbytes)
print(s_hashhex)
#print(s_hashstr)

counter = 0


#WEAK COLLISION TESTING

new_hashbytes = hashbytes # To stars the loop, begin by hashing the initial hash
match_counter = 0 # Run 15 trials
while match_counter != 15:
#while counter < 20:
    #Now, redigest the hash with the old previous cycle's hashbytes
    digest = hashes.Hash(hashes.SHA256())

    digest.update(new_hashbytes)
    new_hashbytes = digest.finalize()
    new_s_hashbytes = new_hashbytes[:3]

    new_s_hashhex = new_s_hashbytes.hex()

    #Since we're comparing the hexes, cut off every 2 values (i.e. 2 hex nums, or 1 byte)
    #if (s_hashhex[:2] == new_s_hashhex[:2]):
        #print("1 Byte Collision Found at cycle: " + str(counter) +  "\n\tOld Hash: " + s_hashhex + "; New Hash: " + new_s_hashhex)

    #if (s_hashhex[:4] == new_s_hashhex[:4]):
    #    print("2 Byte Collision Found at cycle: " + str(counter) +  "\n\tOld Hash: " + s_hashhex + "; New Hash: " + new_s_hashhex)

    if (s_hashhex == new_s_hashhex):
        print("COLLISION #" + str(match_counter+1) + "; CYCLES FOR COLLISION: " + str(counter))
        match_counter += 1
        counter = 0

    counter+=1 