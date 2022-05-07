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

#STRONG COLLISION SETUP
new_hashbytes = hashbytes # To start the loop, begin by using the initial hash 
hasharray = [] # Then, create an array of N 3-byte hash hex strings
for i in range(0, 4096):
    # Now, repeatedly form digests with the old cycle's hashbytes
    # Continue to create an array of hashes of an arbitrary size
    digest = hashes.Hash(hashes.SHA256())
    digest.update(new_hashbytes)
    new_hashbytes = digest.finalize()
    new_s_hashbytes = new_hashbytes[:3]

    new_s_hashhex = new_s_hashbytes.hex()
    hasharray.append(new_s_hashhex)

print("USING A HASH ARRAY OF SIZE: " + str(len(hasharray)))
    
#total = 0

#STRONG COLLISION TESTING
counter = 0 # Counts the number of cycles that the current 
match_counter = 0 # Counts the # of individual trials ran; Testing goes up to 15
while match_counter != 15:
    #Now, form digests with the old previous cycle's hashbytes
    digest = hashes.Hash(hashes.SHA256())

    digest.update(new_hashbytes) #Continues off where the last hashes ended
    new_hashbytes = digest.finalize()
    new_s_hashbytes = new_hashbytes[:3]

    new_s_hashhex = new_s_hashbytes.hex()

    #Run through the entire array and count collisions
    #If a single collision is found in the array, then break (prevents finding duplicate hashes in array)
    for currHash in hasharray:
        if (currHash == new_s_hashhex):
            print("COLLISION #" + str(match_counter+1) + "; CYCLES FOR COLLISION: " + str(counter))
            match_counter += 1
            #total += counter
            counter = 0
            break

    counter+=1 

#print("Average collisions: "+ str(total/15) + " cycles")