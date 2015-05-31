__author__ = 'Kid'

def hash_breaker():
    from Libraries import connectionLib, usefulLibrary
    from termcolor import colored
    import os

    URL_CHALLENGE = "http://ringzer0team.com/challenges/56"
    ERROR_HANDLE = "You are not logged in"
    BEG_MESSAGE = "----- BEGIN HASH -----<br />"   # to retrive the begining of flag
    END_MESSAGE = "<br />"                         # end its end
    session = connectionLib.connect(URL_CHALLENGE, ERROR_HANDLE)
    page_source = connectionLib.getWebpage(session, URL_CHALLENGE)
    challenge = connectionLib.getPayload(page_source, BEG_MESSAGE, END_MESSAGE, 4)

    os.system('cd ringzer0team && generate.py > ../Dicts/hash.txt')     #generate hash list
    answer = usefulLibrary.findSha1Hash('./Dicts/hash.txt', challenge)  #find the hash in hash.txt
    answer = str(answer)
    flag_page = connectionLib.submitPayload(answer, session, URL_CHALLENGE)
    myFlag = connectionLib.getPayload(flag_page, "FLAG", "</div>", -4)
    if myFlag == "":
        return colored('Error, flag not found', 'yellow')
    connectionLib.submitFlag(myFlag, session, URL_CHALLENGE)
    return colored('Flag was found : ', 'green') + myFlag
