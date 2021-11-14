"""
Some functions that create features based on word lists it gets, probably from wordListGenerators
"""
import nltk
import re

def relativeWordDensityFor(words: list[str]):
    def relativeDensity(word: str):
        featureName = f"{word}CountDensity"
        def whatever(blog: str):
            wordFreq = nltk.FreqDist(nltk.tokenize.wordpunct_tokenize(blog))
            return wordFreq[word] / wordFreq.N()
        whatever.__name__ = featureName
        return whatever
    return [relativeDensity(word) for word in words]

def wordPresenceFor(words: list[str]):
    def presence(word: str):
        featureName = f"{word}Presence"
        def whatever(blog: str):
            if re.search(f" {word} ", blog, re.IGNORECASE) is not None:
                return 1
            else:
                return 0
        whatever.__name__ = featureName
        return whatever
    return [presence(word) for word in words]