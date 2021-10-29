from .applyFeatures import applyFeatures, FeatureType
from .jsonParsing import JsonData

def loadDataApplyFeaturesAndSave(
    featuresToApply: dict[str, FeatureType],
    input_path = "./20newsgroups.json",
    specific_output_path = None,
):
    """
    This takes the features to apply to the data in 20newsgroups.json,
    applies them and creates a weka-compatible processedData.json

    The features are to be passed in a dict (aka js object),
    with the name of the feature as key, the feature funktion as value
    """
    # You can pass arguments by name
    jsonData = JsonData(
        input_path = input_path,
        specific_output_path = specific_output_path,
    )
    jsonData.saveToFile(
        applyFeatures(
            featuresToApply,
            jsonData.blogEntries
        )
    )