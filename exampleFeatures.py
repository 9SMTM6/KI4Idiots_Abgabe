"""
Some, probably not interesting for the future, feature functions that I used to test
"""
from typing import Callable


def countAsciiValues(input: str):
    return sum([ord(char) for char in list(input)])

def getLength(input: str):
    return len(input)



def countWordsOfList(input: str)->dict[str,Callable]:
    wordList=["space","image","the","you"]
    funct_dict={}
    for word in wordList:
        funct_dict[f"occ_{word}"]=lambda input: input.count(word)
    
    return funct_dict
