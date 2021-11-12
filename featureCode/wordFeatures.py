"""
Some functions that create features based on word lists it gets, probably from wordListGenerators
"""
import nltk
import re

def relativeWordDensityFor(blog: str, words: list[str]):
    wordFreq = nltk.FreqDist(nltk.tokenize.wordpunct_tokenize(blog))
    return {f"{word}CountDensity": wordFreq[word] / wordFreq.N() for word in words}

def wordPresence(blog: str, words: list[str]):
    return {f"{word}Presence": re.match(f" {word} ", blog, re.IGNORECASE) for word in words}
