__author__ = 'Kid'
# generate_reloaded_again.py > ../Dicts/hash_reloaded_again.txt
# 6 char alphanumeric

tab = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'h', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(0,36) :
    #print tab[i] #1char

    for j in range (0, 36) :
            if j < 36 :
               # print tab[i] + tab[j]   #2char

                for k in range (0, 36) :
                    if k < 36 :
                       # print tab[i] + tab[j] + tab[k]  #3char

                        for l in range (0, 36) :
                            if l < 36 :
                                #print tab[i] + tab[j] + tab[k] + tab[l]  #4char

                                for m in range (0, 36) :
                                                    if m < 36 :
                                                       # print tab[i] + tab[j] + tab[k] + tab[l] + tab[m]  #5char

                                                        for n in range (0, 36) :
                                                                            if n < 36 :
                                                                                var = tab[i] + tab[j] + tab[k] + tab[l] + tab[m] + tab[n]  #6char
                                                                                print(var)
