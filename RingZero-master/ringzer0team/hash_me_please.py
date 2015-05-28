__author__ = 'Aymen'

def hash_me_please():
    from Libraries import connectionLib, usefulLibrary
    from termcolor import colored
    from colorama import init

    URL_CHALLENGE = "http://ringzer0team.com/challenges/13"
    ERROR_HANDLE = "You are not logged in"
    BEG_MESSAGE = "----- BEGIN MESSAGE -----<br />"   # to retrive the begining of flag
    END_MESSAGE = "<br />"                                      # end its end
    session = connectionLib.connect(URL_CHALLENGE, ERROR_HANDLE)
    page_source = connectionLib.getWebpage(session, URL_CHALLENGE)
    challenge = connectionLib.getPayload(page_source, BEG_MESSAGE, END_MESSAGE, 4)
    answer = usefulLibrary.stringTosha512(challenge)
    flag_page = connectionLib.submitPayload(answer, session, URL_CHALLENGE)
    myFlag = connectionLib.getPayload(flag_page, "FLAG", "</div>", -4)
    if myFlag == "":
        return "Error, flag not found"
    connectionLib.submitFlag(myFlag, session, URL_CHALLENGE)
    return colored('Flag was found : ', 'green') + myFlag
