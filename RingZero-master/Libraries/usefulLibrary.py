__author__ = 'Aymen'

# Encode to sha512
def stringTosha512(myString):
    import hashlib
    m = hashlib.sha512()
    m.update(myString.encode('ascii'))
    sha512 = m.hexdigest()
    return sha512

def binaryStringToString(myString):
    import binascii
    n = int('0b' + myString, 2)
    asciiValue = binascii.unhexlify('%x' % n)
    return asciiValue

def hexStringToString(myString):
    import binascii
    d = myString.decode("hex")
    print(d)
    asciiValue = binascii.unhexlify(myString)
    print asciiValue

def findSha1Hash(file, hash):
    f = open(file, "r")
    f.seek(0)
    numb = 0
    for line in f:
        if line == hash + '\n':
             return str(numb)
        numb = numb + 1

def findAndReplaceAscii(msg):

    #ascii numbers
    Zero = "<br />&nbsp;xxx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x<br />x&nbsp;&nbsp;&nbsp;x<br />x&nbsp;&nbsp;&nbsp;x<br />&nbsp;xxx&nbsp;<br />"
    Un = "<br />&nbsp;xx&nbsp;&nbsp;<br />x&nbsp;x&nbsp;&nbsp;<br />&nbsp;&nbsp;x&nbsp;&nbsp;<br />&nbsp;&nbsp;x&nbsp;&nbsp;<br />xxxxx<br />"
    Deux = "<br />&nbsp;xxx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x&nbsp;<br />&nbsp;&nbsp;xx&nbsp;<br />&nbsp;x&nbsp;&nbsp;&nbsp;<br />xxxxx<br />"
    Quatre = "<br />&nbsp;x&nbsp;&nbsp;&nbsp;x<br />x&nbsp;&nbsp;&nbsp;&nbsp;x<br />&nbsp;xxxxx<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br />&nbsp;&nbsp;&nbsp;&nbsp;x<br />"
    Cinq = "<br />xxxxx<br />x&nbsp;&nbsp;&nbsp;&nbsp;<br />&nbsp;xxxx<br />&nbsp;&nbsp;&nbsp;&nbsp;x<br />xxxxx"
    Huit = "<br />&nbsp;xxx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x<br />&nbsp;&nbsp;xx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x<br />&nbsp;xxx&nbsp;<br />"

    #remplace values
    msg = msg.replace(Zero, '0')
    msg = msg.replace(Un, '1')
    msg = msg.replace(Deux, '2')
    msg = msg.replace(Quatre, '4')
    msg = msg.replace(Cinq, '5')
    msg = msg.replace(Huit, '8')
    msg = msg.replace("<br /><br />", '') # end of msg
    msg = msg.rstrip() # remove whitespaces

    return msg

def fileExist(filePath):
    import os
    return os.path.exists(filePath)

def createFile(filePath):
    f = open(filePath, 'w')
    f.close()

def appendToFile(filePath, text):
    f = open(filePath, 'a+')
    f.write(text)
    f.close()

def readFile(filePath):
    f = open(filePath, 'r')
    text = f.read()
    return text

def delteFile(filePath):
    import os
    if fileExist(filePath):
        os.remove(filePath)

def lookForString(filePath, text):
    f = open(filePath, "r")
    f.seek(0)
    flagExist = False
    for line in f:
        if line == text:
            flagExist = True
    f.close()
    return flagExist

def getUHID():
    import sys
    currentOS = sys.platform
    uhid = ""
    if (currentOS == "win32") or (currentOS == "cygwin"):
        import platform
        if platform.python_version()[0] == "3":
           import winreg as wreg
        elif platform.python_version()[0] == "2":
           import _winreg as wreg
        try:
            key = wreg.OpenKey(
                                wreg.HKEY_LOCAL_MACHINE,
                                 "SOFTWARE\\Microsoft\\Cryptography",
                                 0,
                                 wreg.KEY_READ | wreg.KEY_WOW64_64KEY
                                )

            uhid = stringTosha512(wreg.QueryValueEx(key, "MachineGuid")[0])
        except ():
            exit("Unable to generate secret cryptographyc key" )
    elif currentOS == "darwin":
        uhid = stringTosha512(subprocess.check_output(
            ('system_profiler | grep -i "Serial Number (system):"' + " | awk '{print $4}'")
            .split()).decode('ascii'))
    else:
        import subprocess
        uhid = stringTosha512(subprocess.check_output(
                'hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid'
                .split()).decode('ascii'))
    return uhid


def encryptData( username, password):
    import random
    toCrypt = username + '\n' + password + '\n'
    key = getUHID()
    if len(toCrypt) > len(key):
        exit("username or passweord length too big !")
    while len(toCrypt) < len(key):
        toCrypt += chr(random.randrange(0, 255))
    encrypted = ""
    for i in range(len(toCrypt)):
        encrypted += chr(ord(toCrypt[i]) ^ ord(key[i % len(key)]))
    return encrypted


def decryptData(toDerypt):
    key = getUHID()
    decrypted = ""
    for i in range(len(toDerypt)):
        decrypted += chr(ord(toDerypt[i]) ^ ord(key[i % len(key)]))
    decrypted = decrypted.split("\n")
    return decrypted[0], decrypted[1]