from datasetSplit import RandomSplit
from exampleFeatures import getLength, countAsciiValues
from featureApplication import applyFeatures, JsonData
from featureCode import *
from math import log

#import wordlist
wordList=[]
with open("wordList.txt") as words:
    for line in words:
        wordList.append(line.removesuffix("\n"))

def main():
    name = "20newsgroups"
    RandomSplit(
        name,
        seed = countAsciiValues("KI4Idiots"),
        partForTrainAndCompare = 0.2,
    ).saveToFiles(name)
    
    data = JsonData("./20newsgroups_train")
    distributions = wordDistributionsById(data)

    appliedFeatures = {
        **relativeWordDensityFor(getWordsOf(
            rankWith(
                distributions,
                lambda word, dist, commonDist: dist[word] / commonDist[word] * log(dist[word]) / log(dist.N()),
            ),
            rankToByCat=40,
        )),
        "countCharsWWhitespace": len,
        "lexicalDiversity": lexicalDiversityStemmedNostop,
        "totalWordCount": total_word_count,
        "count_chars": count_chars_ignore_whitespace,
        "average_word_length": average_word_length,
        "max_word_length": max_word_length,
        "avg_sent_length": avg_sentence_length,
    }
    for version in ["train", "compare", "validate"]:
        # You can pass arguments by name
        jsonData = JsonData(input_name = f"{name}_{version}")
        jsonData\
            .addData(
                applyFeatures(
                    appliedFeatures,
                    jsonData.blogEntries
                )
            )\
            .saveToFile()

# Das ist ein wenig nerfig bei python, wenn man von einem anderen file importiert
#  wird alles in dem file ausgeführt.
#
# Diese aufrage vermeidet das, der __name__ ist eine variable die pro file gesetzt wird, 
# und nur auf __main__ ist wenn dies das original gestartete file ist.
# Um das ein wenig in die bekannte form mit einer main funktion zu bringen ist es üblich
# eine solche zu definieren und hier aufzurufen, wie ich hier getan habe
if __name__ == "__main__":
    main()
