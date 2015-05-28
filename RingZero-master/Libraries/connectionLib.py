__author__ = 'Aymen'
import requests
from Libraries import usefulLibrary
from main import DOMAIN, CHALLENGES

USERNAME = ""
PASSWORD = ""

credsPath = CHALLENGES + ".credentials"

# authentificating
def connect(url, errorHandling = ""):
    if url.find("ringzer0team") > -1:
        global PASSWORD, USERNAME
        if (USERNAME == "") or (PASSWORD == ""):
            creds = usefulLibrary.readFile(credsPath)
            creds = usefulLibrary.decryptData(creds)
            USERNAME = creds[0]
            PASSWORD = creds[1]
        credentials = {'username': USERNAME, 'password': PASSWORD}
        session = requests.Session()
        login_response = session.post(DOMAIN+"/login", data=credentials)
        if errorHandling != "":
            if errorHandling in login_response.text:
                usefulLibrary.delteFile(credsPath)
                print("Error, failed to login ! Please try again")
        return session
    else:
        exit("Only accept " + DOMAIN + " domain for now")

# Getting the webpage
def getWebpage(session, url):
    challenge = session.get(url)
    page_source = challenge.text  # Page_source contains all the web page source in a single sting
    return page_source

def getPayload(page_source, beg_message, end_message, beg_padding=0, end_padding=0, reverse = False):  # To do : implement regex

    if beg_message == '':
        beg = 0
    elif not reverse:
        beg = page_source.find(beg_message, 0, len(page_source))
    else:
        beg = page_source.rfind(beg_message, 0, len(page_source))
    if beg == -1:
        return ""
    else:
        beg += len(beg_message) + beg_padding

    if end_message == '':
        end = len(page_source)
    elif not reverse:
        end = page_source.find(end_message, beg, len(page_source))
    else:
        end = page_source.rfind(end_message, beg, len(page_source))
    if end == -1:
        return ""
    else:
        end -= end_padding

    payload = ""
    payload += page_source[beg:end]
    return payload

# Send payload flag
def submitPayload(payload, session, url):
    connectTo = url + "/" + payload
    return getWebpage(session, connectTo)

def getChallengeName(session, challengeID):
    relativePath = '<a href="/challenges/'+challengeID+' ">'
    url = DOMAIN + "/challenges"
    page_source = getWebpage(session, url)
    name = getPayload(page_source, relativePath, "</a>")
    return name

def getChallengeCategorie(session, challengeID):
    relativePath = '<a href="/challenges/'+challengeID+' ">'
    url = DOMAIN + "/challenges"
    page_source = getWebpage(session, url)

    categorie = getPayload(page_source, '', relativePath)
    categorie = getPayload(categorie, '<h4 class="title_hover" data-id=', '', 0, 0, True)
    categorie = getPayload(categorie, '">', ' (<')
    return categorie

# Send flag
def submitFlag(flag, session, url):
    # we add the flag to out databse
    addFlagToFile(getFlagID(flag, session, url))
    # And now send the flag to the server
    credentials = {'flag': flag}
    status = session.post(url, data=credentials)
    return status  # useless

def getFlagID(flag, session, url):
    # format flag
    challengeID = url.split('/')[-1]
    challengeName = getChallengeName(session, challengeID)
    challengeCat = getChallengeCategorie(session, challengeID)
    flagID = flag + ";" + challengeCat + ';' + challengeName + ';' + challengeID + ';' + url + "\n"
    return flagID

def addFlagToFile(flagID):
    # Lets save the flag in the flag file !
    # we create prepare the file
    filePath = "Flags/"+CHALLENGES+".csv"
    if not usefulLibrary.fileExist(filePath):
        usefulLibrary.createFile(filePath)
        usefulLibrary.appendToFile(filePath, "Flag;Category;Name;ID;URL\n")

    # Check if flag exist already
    if not usefulLibrary.lookForString(filePath, flagID):
        usefulLibrary.appendToFile(filePath, flagID)