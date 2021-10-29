from exampleFeatures import *
from applyFeatures import applyFeatures
from jsonParsing import JsonData

def main():
    jsonData = JsonData()
    jsonData.saveToFile(applyFeatures(
        [getLength, countAsciiValues],
        jsonData.blogEntries
    ))

if __name__== "__main__":
    main()