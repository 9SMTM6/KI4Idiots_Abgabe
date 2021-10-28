from exampleFeatures import *
from applyFeatures import applyFeatures

def main():
    print(applyFeatures([getLength, countAsciiValues], ["a", "aaa", "aaaaaaa"]))

if __name__== "__main__":
    main()