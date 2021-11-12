"""
Some functions that create features based on word lists it gets, probably from wordListGenerators
"""
import nltk
import re

def relativeWordDensityFor(words: list[str]):
    def relativeDensity(word: str):
        def whatever(blog: str):
            wordFreq = nltk.FreqDist(nltk.tokenize.wordpunct_tokenize(blog))
            return wordFreq[word] / wordFreq.N()
        return whatever        
    return {f"{word}CountDensity": relativeDensity(word) for word in words}

def wordPresence(words: list[str]):
    def presence(word: str):
        def whatever(blog: str):
            return re.match(f" {word} ", blog, re.IGNORECASE)
        return whatever        
    return {f"{word}CountDensity": presence(word) for word in words}