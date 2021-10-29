"""
These functions are meant to apply our features to the data in a generic way
"""

from typing import Callable, Iterable

# types, functions, Classes, pretty much everything can be assigned to variables
FeatureType = Callable[[str], float]
"""A function that takes a string as only parameter and returns a floating point number"""

def applyFeature(feature: FeatureType, blogEntries: Iterable[str]) -> list[float]:
    # this is using list comprehension, in other languages, eg JS, Array.map fulfills the same role
    return [feature(blog) for blog in blogEntries]

def applyFeatures(features: dict[str, FeatureType], blogEntries: Iterable[str]) -> dict[str, list[str]]:
    # and this is dictionary comprehension
    return {key: applyFeature(feature, blogEntries) for key, feature in features.items()}
