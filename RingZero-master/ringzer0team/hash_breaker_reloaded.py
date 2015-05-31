__author__ = 'Kid'

def hash_breaker_reloaded():
    from Libraries import connectionLib, usefulLibrary
    from termcolor import colored
    import os

    URL_CHALLENGE = "http://ringzer0team.com/challenges/57"
    ERROR_HANDLE = "You are not logged in"
    BEG_HASH = "----- BEGIN HASH -----<br />"            # to retrive the hash
    END_HASH = "<br />"
    BEG_SALT = "----- BEGIN SALT -----<br />"            # to retrive the salt
    END_SALT = "<br />"                                  # its end
    session = connectionLib.connect(URL_CHALLENGE, ERROR_HANDLE)
    page_source = connectionLib.getWebpage(session, URL_CHALLENGE)
    hash = connectionLib.getPayload(page_source, BEG_HASH, END_HASH, 4) # the hash
    salt = connectionLib.getPayload(page_source, BEG_SALT, END_SALT, 4) # the salt

    os.system('cd ringzer0team && generate_reloaded.py --salt ' + salt + ' > ../Dicts/hash_reloaded.txt') #generate hash list with salt
    answer = usefulLibrary.findSha1Hash('./Dicts/hash_reloaded.txt', hash)  #find the hash in the list

    flag_page = connectionLib.submitPayload(answer, session, URL_CHALLENGE)
    myFlag = connectionLib.getPayload(flag_page, "FLAG", "</div>", -4)
    if myFlag == "":
        return colored('Error, flag not found', 'yellow')
    connectionLib.submitFlag(myFlag, session, URL_CHALLENGE)
    return colored('Flag was found : ', 'green') + myFlag