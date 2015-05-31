__author__ = 'Kid'
# generate_reloaded.py --salt THESALT > ../Dicts/hash_reloaded.txt
# the number of the line is the int value of the hash

import sys, getopt, hashlib

def main(argv):

   try:
      opts, args = getopt.getopt(argv,"s",["salt="])
   except getopt.GetoptError:
      print 'generate_reloaded.py --salt SALT > ../Dicts/hash_reloaded.txt'
      sys.exit(2)

   for opt, arg in opts:
      if opt in ("--salt"):
         salt = arg
         var = '0'  #from 0 to 9999

         while var <= '9999':
             hash = hashlib.sha1(var.encode('utf-8') + salt.encode('utf-8')).hexdigest()
             print hash

             var = int(var) + 1  #gen next number
             var = str(var)      #convert to str for hashlib fonction

      else:
         print ('generate_reloaded.py --salt SALT > ../Dicts/hash_reloaded.txt')
         sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])
