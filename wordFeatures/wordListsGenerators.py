from typing import Callable, Optional
from math import log
import nltk

import sys

from nltk.probability import FreqDist
sys.path.append("C:/Users/smaier/Documents/Workspace/ki/KI4Idiots_Abgabe")

from featureApplication import JsonData
from nltk.corpus import stopwords

def main():
    data = JsonData("./20newsgroups_train")
    distributions = wordDistributionsByIdAndCommonDist(data)

    wordsv1 = getWordsOf(
        rankWith(
            distributions,
            lambda word, dist, commonDist: dist[word] / commonDist[word] * log(dist[word]) / log(dist.N()),
        ),
        takeToByCat=40,
    )

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

def wordDistributionsByIdAndCommonDist(data: JsonData) -> tuple[list[FreqDist], FreqDist]:
    distributions = [
        FreqDist(tagAndExclude(removeStopWords(tokenizeAndCombine(data.blogEntriesById[str(id)]))))
        for id in range(4)
    ]
    return (
        distributions,
        FreqDist(list(distributions[0].elements()) + list(distributions[1].elements()) + list(distributions[2].elements()) + list(distributions[3].elements()))    
    )

def stemmedWordDistributionsByIdAndCommonDist(data: JsonData) -> tuple[list[FreqDist], FreqDist]:
    stemmer = nltk.PorterStemmer()
    distributions = [
        FreqDist(stemmer.stem(token) for token in tagAndExclude(removeStopWords(tokenizeAndCombine(data.blogEntriesById[str(id)]))))
        for id in range(4)
    ]
    return (
        distributions,
        FreqDist(list(distributions[0].elements()) + list(distributions[1].elements()) + list(distributions[2].elements()) + list(distributions[3].elements()))    
    )

def rankWith(distributionsAndCommon: tuple[list[FreqDist], FreqDist], rankFn: Callable[[str, FreqDist, FreqDist], float]):
    """Ranks the provided ditributions using the rankFn. rankFn takes the word to rank, and 2 FreqDist, (source of the word, a combined one)"""
    (distributions, commondist) = distributionsAndCommon
    distsWithRank: list[list[tuple[str, float]]] = []
    for id in range(4):
        dist = distributions[id]
        distsWithRank.append([])
        for word in dist.keys():
            distsWithRank[id].append((word, rankFn(word, dist, commondist)))
    sortedDists = [sorted(dist, key=lambda a: a[1], reverse= True) for dist in distsWithRank]
    return sortedDists

def getWordsOf(input: list[list[tuple[str, float]]], cutoff: Optional[float] = None, takeToByCat: Optional[int] = None, takeTotal: Optional[int] = None):
    outputByCat: list[list[str]] = []
    for dist in input:
        outputByCat.append([(word, val) for (word, val) in dist if (cutoff is None or val>cutoff)][:takeToByCat])
    output: list[str] = []
    for out in outputByCat:
        output += out
    return [word for (word, _) in sorted(output, key=lambda a: a[1], reverse= True)][:takeTotal]

if __name__ == "__main__":
    main()