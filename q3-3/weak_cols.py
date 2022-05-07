from cryptography.hazmat.primitives import hashes
import random

#First, generate some random bytes
#   This is hashed and used as the initial hash
random.seed()
randbytes = random.randbytes(16) 
digest = hashes.Hash(hashes.SHA256())
digest.update(randbytes)

#Grab the first 3 bytes of a randomly generated hash
hashbytes = digest.finalize()
s_hashbytes = hashbytes[:3]
s_hashhex = s_hashbytes.hex()

#WEAK COLLISION TESTING
counter = 0 # Counts the number of cycles that the current 
new_hashbytes = hashbytes # To start the loop, begin by hashing the initial hash
match_counter = 0 # Counts the # of individual trials ran; Testing goes up to 15
while match_counter != 15:
#while counter < 20:
    #Now, form digests with the old previous cycle's hashbytes
    digest = hashes.Hash(hashes.SHA256())

    digest.update(new_hashbytes)
    new_hashbytes = digest.finalize()
    new_s_hashbytes = new_hashbytes[:3]

    new_s_hashhex = new_s_hashbytes.hex()

    #Since we're comparing the hexes, cut off every 2 values (i.e. 2 hex nums, or 1 byte)
    #   The final version only includes comparisons for 3 bytes, but I included for 1 and 2 bytes as well to sate my curiosity
    #if (s_hashhex[:2] == new_s_hashhex[:2]):
        #print("1 Byte Collision Found at cycle: " + str(counter) +  "\n\tOld Hash: " + s_hashhex + "; New Hash: " + new_s_hashhex)

    #if (s_hashhex[:4] == new_s_hashhex[:4]):
    #    print("2 Byte Collision Found at cycle: " + str(counter) +  "\n\tOld Hash: " + s_hashhex + "; New Hash: " + new_s_hashhex)

    if (s_hashhex == new_s_hashhex):
        print("COLLISION #" + str(match_counter+1) + "; CYCLES FOR COLLISION: " + str(counter))
        match_counter += 1
        counter = 0

    counter+=1 