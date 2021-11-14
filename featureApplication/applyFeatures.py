"""
These functions are meant to apply our features to the data in a generic way
"""

import pickle
from typing import Callable, Iterable, NamedTuple

class CachedFeatureDetails(NamedTuple):
    name: str
    code: bytes
    returnValue: list[float]

# types, functions, Classes, pretty much everything can be assigned to variables
FeatureType = Callable[[str], float]
"""A function that takes a string as only parameter and returns a floating point number"""

def applyFeature(feature: FeatureType, blogEntries: Iterable[str]) -> list[float]:
    # this is using list comprehension, in other languages, eg JS, Array.map fulfills the same role
    return [feature(blog) for blog in blogEntries]

def applyFeatures(features: dict[str, FeatureType], blogEntries: Iterable[str]) -> dict[str, list[str]]:
    """
    The features are to be passed in a list,
    The name of the function will serve as feature-name, the return value of the feature value
    """
    cacheFilename = "featureCache.pickle"
    try: 
        with open(cacheFilename, "br") as file:
            cache = pickle.load(file)
            featureResults: dict[str, CachedFeatureDetails] = cache[0]
            # invalidate cache if it was created with different blogEntries
            if blogEntries != cache[1]:
                featureResults = {}
    except:
        featureResults = {}

    # Calculate any features that were not cached, or whos functions changed in the meantime
    for feature in features:
        featureName = feature.__name__
        featureCode = feature.__code__.co_code
        if featureResults.get(featureName) is None or featureResults[featureName].code != featureCode:
            print(f"Recalculating {featureName}")
            featureResults[featureName] = CachedFeatureDetails(featureName, featureCode, applyFeature(feature, blogEntries))
        else:
            print(f"Loaded {featureName} from cache")
    
    with open(cacheFilename, "bw") as file:
        pickle.dump((featureResults, blogEntries), file)
    
    return {feature.name: feature.returnValue for (_, feature) in featureResults.items()}
