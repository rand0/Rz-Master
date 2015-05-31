__author__ = 'Aymen'
from ringzer0team import ascii_art, hash_me_please, hash_breaker, hash_breaker_reloaded, hash_breaker_reloaded_again, hash_me_reloaded, equation
from termcolor import colored

challenges = {119 : ascii_art.ascii_art,
              32 : equation.equation,
              56 : hash_breaker.hash_breaker,
              57 : hash_breaker_reloaded.hash_breaker_reloaded,
              #159 : hash_breaker_reloaded_again.hash_breaker_reloaded_again, #dont work
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