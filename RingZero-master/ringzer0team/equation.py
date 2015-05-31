__author__ = 'Kid'

def equation():
    from Libraries import connectionLib, usefulLibrary
    from termcolor import colored

    URL_CHALLENGE = "http://ringzer0team.com/challenges/32"
    ERROR_HANDLE = "You are not logged in"
    BEG_MESSAGE = "----- BEGIN MESSAGE -----<br />"   # to retrive the begining of flag
    FIRST = " + 0x"
    SECOND = " -"
    END_MESSAGE = "= ?<br />"                         # end its end
    session = connectionLib.connect(URL_CHALLENGE, ERROR_HANDLE)
    page_source = connectionLib.getWebpage(session, URL_CHALLENGE)

    #Values
    first = connectionLib.getPayload(page_source, BEG_MESSAGE, FIRST, 4) #int
    second = '0' + connectionLib.getPayload(page_source, first, SECOND, 4) #hex
    third = '1' + connectionLib.getPayload(page_source, second, END_MESSAGE, 4) #bin
    #challenge = connectionLib.getPayload(page_source, BEG_MESSAGE, END_MESSAGE, 4) # print challenge for debugging

    answer = str(int(first) + int(second, 16) - int(third, 2))
    flag_page = connectionLib.submitPayload(answer, session, URL_CHALLENGE)
    myFlag = connectionLib.getPayload(flag_page, "FLAG", "</div>", -4)
    if myFlag == "":
        return colored('Error, flag not found', 'yellow')
    connectionLib.submitFlag(myFlag, session, URL_CHALLENGE)
    return colored('Flag was found : ', 'green') + myFlag
