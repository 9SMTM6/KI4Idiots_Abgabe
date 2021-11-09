from datasetSplit import RandomSplit
from exampleFeatures import getLength, countAsciiValues
from featureApplication import applyFeatures, JsonData
from featureCode.lexical_diversity import lexicalDiversityLemmatizedNostop
from featureCode.specificWordCount import countWordsOfList
from featureCode.total_word_count import total_word_count


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
    "lexicalDiversity": lexicalDiversityLemmatizedNostop,
    "totalWorCount": total_word_count,
}

def main():
    name = "20newsgroups"
    RandomSplit(
        name,
        seed = countAsciiValues("KI4Idiots"),
        partForTrainAndCompare = 0.2,
    ).saveToFiles(name)
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
