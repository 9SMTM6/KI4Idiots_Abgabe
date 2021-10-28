from exampleFeatures import *
from applyFeatures import applyFeatures
from jsonParsing import loadData

def main():
    print(loadData())
    print(applyFeatures([getLength, countAsciiValues], ["a", "aaa", "aaaaaaa"]))

if __name__== "__main__":
    main()