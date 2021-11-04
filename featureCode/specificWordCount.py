from typing import Callable


def countWordsOfList(wordList)->dict[str,Callable]:
    "add new word-count-feature for each word in wordList"

    #define new function to create each wordcount function
    def countWord(word):
        return lambda input: input.count(word)

    #declare variable to store features
    feature_dict={}

    #add feature for each word
    for word in wordList:
        feature_dict[f"freq_{word}"]=countWord(word)
    
    return feature_dict