from exampleFeatures import *
from applyFeatures import applyFeatures, FeatureType
from jsonParsing import JsonData

appliedFeatures = {
    "textLenght": getLength,
    "asciiValueSum": countAsciiValues,
}

def main():
    loadDataApplyFeaturesAndSave(appliedFeatures)

def loadDataApplyFeaturesAndSave(featuresToApply: dict[str, FeatureType]):
    """"
    This takes the features to apply to the data in 20newsgroups.json,
    applies them and creates a weka-compatible processedData.json

    The features are to be passed in a dict (aka js object),
    with the name of the feature as key, the feature funktion as value
    """
    jsonData = JsonData()
    jsonData.saveToFile(
        applyFeatures(
            featuresToApply,
            jsonData.blogEntries
        )
    )

# Das ist ein wenig nerfig bei python, wenn man von einem anderen file importiert
#  wird alles in dem file ausgeführt.
#
# Diese aufrage vermeidet das, der __name__ ist eine variable die pro file gesetzt wird, 
# und nur auf __main__ ist wenn dies das original gestartete file ist.
# Um das ein wenig in die bekannte form mit einer main funktion zu bringen ist es üblich
# eine solche zu definieren und hier aufzurufen, wie ich hier getan habe
if __name__== "__main__":
    main()