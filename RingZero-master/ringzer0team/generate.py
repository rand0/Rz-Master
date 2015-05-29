__author__ = 'Kid'
# generate.py > ../Dicts/hash.txt
# the number of the line is the int value of the hash

import hashlib, os

var = '0'  #from 0 to 9999
while var <= '9999':
    hash_object = hashlib.sha1(var)
    hash = hash_object.hexdigest()
    print(hash)
    var = int(var) + 1  #gen next number
    var = str(var)      #convert to str for hashlib fonction
