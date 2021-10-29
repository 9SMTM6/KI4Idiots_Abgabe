from typing import Callable, Iterable

FeatureType = Callable[[str], float]

def applyFeature(feature: FeatureType, blogEntries: Iterable[str]) -> list[float]:
    return [feature(blog) for blog in blogEntries]

def applyFeatures(features: Iterable[FeatureType], blogEntries: Iterable[str]) -> dict[list[str]]:
    return {feature.__name__: applyFeature(feature, blogEntries) for feature in features}
