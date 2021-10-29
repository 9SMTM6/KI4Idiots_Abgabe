from featureApplication import loadDataApplyFeaturesAndSave
from datasetSplit import RandomSplit
from exampleFeatures import getLength, countAsciiValues
import json

appliedFeatures = {
    "textLenght": getLength,
    "asciiValueSum": countAsciiValues,
}

def main():
    name = "20newsgroups"
    loadDataApplyFeaturesAndSave(
        appliedFeatures,
        input_path = f"{name}.json",
    )
    with open(f"./{name}_processed.json") as filePointer:
        split = RandomSplit(json.load(filePointer), seed = countAsciiValues("KI4Idiots"))
    split.saveToFiles(name)


# Das ist ein wenig nerfig bei python, wenn man von einem anderen file importiert
#  wird alles in dem file ausgeführt.
#
# Diese aufrage vermeidet das, der __name__ ist eine variable die pro file gesetzt wird, 
# und nur auf __main__ ist wenn dies das original gestartete file ist.
# Um das ein wenig in die bekannte form mit einer main funktion zu bringen ist es üblich
# eine solche zu definieren und hier aufzurufen, wie ich hier getan habe
if __name__ == "__main__":
    main()