from typing import Callable


def countWordsOfList(wordList)->dict[str,Callable]:
    def countWord(word):
        return lambda input: input.count(word)
    funct_dict={}
    for word in wordList:
        funct_dict[f"occ_{word}"]=countWord(word)
    
    return funct_dict