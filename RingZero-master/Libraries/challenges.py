__author__ = 'Aymen'
from ringzer0team import hash_me_please, hash_me_reloaded, equation
from termcolor import colored
from colorama import init

challenges = {32 : equation.equation,
              13 : hash_me_please.hash_me_please,
              14 : hash_me_reloaded.hash_me_reloaded
             }

def challenge(value):
    return colored(' +','white') + colored(challenges[value].__name__, 'yellow') + colored(' ---> ', 'white') + challenges[value]() + '\n'

def doAll():
    print ("-Here's your flags !")
    output = ""
    for key in challenges.keys():
        output += challenge(key)
    return output