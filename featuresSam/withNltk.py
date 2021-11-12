from typing import Optional
from math import log
import nltk

import sys
sys.path.append("C:/Users/smaier/Documents/Workspace/ki/KI4Idiots_Abgabe")

from featureApplication import *
from nltk.corpus import stopwords

def main():
    data = JsonData("./20newsgroups_train")
    distributions = wordDistributionsById(data)

    wordsv1 = getWordsOf(rankVersion1(distributions), rankToByCat=30)

    print(wordsv1)

def tokenizeAndCombine(input: list[str]):
    tokens: list[str] = []
    for entry in input:
        tokens += nltk.tokenize.word_tokenize(entry) # this excludes file endings: if word.isalnum()
    return tokens

def tagAndExclude(input: list[str]):
    """takes a ist of tokens, tags them, excludes words with uninteresting tags"""
    excludedWordTags = ['.', 'ADP', 'DET', "PRON", "PRT", "CONJ"]

    whiteList = ["NOUN", "VERB", "ADJ", "X"]

    unknownList = ["ADV", "NUM"]
    wordtokens: list[tuple[str, str]] = nltk.pos_tag(input, tagset = 'universal')
    return [word for (word, tag) in wordtokens if tag in whiteList]

stopwords: list[str] = stopwords.words("english")

def removeStopWords(input: list[str]):
    return [word for word in input if word not in stopwords]

def wordDistributionsById(data: JsonData) -> list[nltk.FreqDist]:
    return [
        nltk.FreqDist(tagAndExclude(removeStopWords(tokenizeAndCombine(data.blogEntriesById[str(id)]))))
        for id in range(4)
    ]

def rankVersion1(distributions: list[nltk.FreqDist]):
    """V1 of the ranking, per category"""
    commondist = nltk.FreqDist(list(distributions[0].elements()) + list(distributions[1].elements()) + list(distributions[2].elements()) + list(distributions[3].elements()))
    distsWithRank: list[list[tuple[str, float]]] = []
    for id in range(4):
        dist = distributions[id]
        distsWithRank.append([])
        for word in dist.keys():
            distsWithRank[id].append((word, dist[word] / commondist[word] * log(dist[word]) / log(dist.N()), dist[word])) #dist[word] / commondist[word] * log(dist[word]) / log(dist.N())
    sortedSelectedDists = [sorted(dist, key=lambda a: a[1], reverse= True) for dist in distsWithRank]
    return sortedSelectedDists

def getWordsOf(input: list[list[tuple[str, float]]], cutoff: Optional[float] = None, rankToByCat: int = -1, rankTotal: int = -1):
    outputByCat: list[list[str]] = []
    for dist in input:
        outputByCat.append([word for (word, val,_) in dist if (cutoff is None or val>cutoff)][:rankToByCat])
    output: list[str] = []
    for out in outputByCat:
        output += out
    return output

if __name__ == "__main__":
    main()