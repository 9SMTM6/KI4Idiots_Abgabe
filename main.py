from datasetSplit import RandomSplit
from exampleFeatures import getLength, countAsciiValues
from featureApplication import applyFeatures, JsonData
from featureCode.specificWordCount import countWordsOfList
from featureCode.lexical_diversity import lexicalDiversity


#import wordlist
wordList=[]
with open("wordList.txt") as words:
    for line in words:
        wordList.append(line.removesuffix("\n"))


appliedFeatures = {
    **countWordsOfList(wordList),
    "textLenght": getLength,
    "asciiValueSum": countAsciiValues,
    "textLength": len,
    "lexicalDiversity": lexicalDiversity,
}

def main():
    name = "20newsgroups"
    # You can pass arguments by name
    jsonData = JsonData(input_name = name)
    jsonData\
        .addData(
            applyFeatures(
                appliedFeatures,
                jsonData.blogEntries
            )
        )\
        .saveToFile()
    RandomSplit(
        f"{name}_processed",
        seed = countAsciiValues("KI4Idiots"),
        partForTrainAndCompare = 0.1,
    ).saveToFiles(name)


# Das ist ein wenig nerfig bei python, wenn man von einem anderen file importiert
#  wird alles in dem file ausgeführt.
#
# Diese aufrage vermeidet das, der __name__ ist eine variable die pro file gesetzt wird, 
# und nur auf __main__ ist wenn dies das original gestartete file ist.
# Um das ein wenig in die bekannte form mit einer main funktion zu bringen ist es üblich
# eine solche zu definieren und hier aufzurufen, wie ich hier getan habe
if __name__ == "__main__":
    main()
