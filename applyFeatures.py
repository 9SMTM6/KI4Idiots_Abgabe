from typing import Callable, Iterable

FeatureType = Callable[[str], float]

def applyFeature(feature: FeatureType, blogEntries: Iterable[str]) -> list[float]:
    return [feature(blog) for blog in blogEntries]

def applyFeatures(features: Iterable[FeatureType], blogEntries: Iterable[str]) -> list[list[str]]:
    return [applyFeature(feature, blogEntries) for feature in features]
