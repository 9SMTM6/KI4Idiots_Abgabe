import pickle
from datasetSplit import RandomSplit
from exampleFeatures import countAsciiValues
from featureApplication import applyFeatures, JsonData
from wordFeatures import *
import featureCode as f
from math import log

name = "20newsgroups"
random_seed =  countAsciiValues("KI4Idiots")
random_split = 0.2

def main():
    rankings = getWordListRankings()

    appliedFeatureCombinations = {
        "allSimpleFeatures": [
            f.max_word_length,
            f.average_word_length,
            f.avg_sentence_length,
            f.count_chars_ignore_whitespace,
            f.count_chars_with_whitespace,
            f.lexicalDiversity,
            f.lexicalDiversityStemmed,
            f.lexicalDiversityStemmedNostop,
            f.lexicalDiversityLemmatized,
            f.lexicalDiversityLemmatizedNostop,
        ],
        "wordPresenceByCountAndPrevalence": [
            *wordPresenceFor(getWordsOf(
                rankings["relativeWordCountAndPrevalenceMagnitude"],
                takeToByCat=100,
            )),
        ],
        "relativeWordCountByRelativeCount": [
            *relativeWordDensityFor(getWordsOf(
                rankings["relativeWordCount"],
                takeToByCat=70,
            )),
        ],
        "samuelsSelectionNaiveLog40": [
            *relativeWordDensityFor(getWordsOf(
                rankings["relativeWordCountAndPrevalenceMagnitude"],
                takeToByCat=40,
            )),
            f.lexicalDiversityLemmatizedNostop,
            f.max_word_length,
            f.average_word_length,
            f.avg_sentence_length,
        ],
        "samuelsSelectionStemmedRegex40": [
            *relativeWordDensityRegexMatchFor(getWordsOf(
                rankings["relativeStemmedWordCountAndPrevalenceMagnitude"],
                takeToByCat=40,
            )),
            f.lexicalDiversityLemmatizedNostop,
            f.max_word_length,
            f.average_word_length,
            f.avg_sentence_length,
        ],
        "samuelsSelectionStemmedRegex100": [
            *relativeWordDensityRegexMatchFor(getWordsOf(
                rankings["relativeStemmedWordCountAndPrevalenceMagnitude"],
                takeToByCat=100,
            )),
            f.lexicalDiversityLemmatizedNostop,
            f.max_word_length,
            f.average_word_length,
            f.avg_sentence_length,
        ],
        "samuelsSelectionStemmedRegexSingled100": [
            *relativeWordDensityRegexMatchFor(getWordsOf(
                rankings["relativeSingledStemmedWordPrevalenceMagintude"],
                takeToByCat=100,
            )),
            f.lexicalDiversityLemmatizedNostop,
            f.max_word_length,
            f.average_word_length,
            f.avg_sentence_length,
        ],
        "samuelsSelectionTrial": [
            *relativeWordDensityFor(getWordsOf(
                rankings["relativeWordCountAndPrevalenceTrial"],
                takeToByCat=40,
            )),
            f.lexicalDiversityLemmatizedNostop,
            f.max_word_length,
            f.average_word_length,
            f.avg_sentence_length,
        ],
    }
    for key, featureList in appliedFeatureCombinations.items():
        # You can pass arguments by name
        jsonData = JsonData(input_name = name)
        processed_name = f"output/{key}_processed"
        processed_name_with_text = f"output/withText/{key}_processed"
        featureResults = applyFeatures(
            featureList,
            jsonData.blogEntries,
        )

        jsonData\
            .addData(featureResults)\
            .saveToFile(processed_name)
        RandomSplit(
            processed_name,
            seed = random_seed,
            partForTrainAndCompare = random_split,
        ).saveToFiles(processed_name)

        jsonData = JsonData(input_name = name)
        jsonData\
            .addData(featureResults, keepText = True)\
            .saveToFile(processed_name_with_text)
        RandomSplit(
            processed_name_with_text,
            seed = random_seed,
            partForTrainAndCompare = random_split,
        ).saveToFiles(processed_name_with_text)

def getWordListRankings() -> dict[str, list[list[tuple[str, float]]]]:
    cacheFileName = "wordCountLists.pickle"

    calcFnCode = calcWordListRankings.__code__.co_code

    try:
        with open(cacheFileName, "br") as file:
            cached = pickle.load(file)
        if cached[0] != calcFnCode:
            raise "whatever"
        rankings = cached[1]
        print("Using wordlists from cache")
    except:
        print("Recalculating wordlists")
        
        RandomSplit(
            name,
            seed = random_seed,
            partForTrainAndCompare = random_split,
        ).saveToFiles(name)
        
        data = JsonData("./20newsgroups_train")
        rankings = calcWordListRankings(data)

    with open(cacheFileName, "bw") as file:
        pickle.dump((calcFnCode, rankings), file)
    return rankings

def calcWordListRankings(data: JsonData):
    rankings: dict[str, list[list[tuple[str, float]]]] = {}

    distributionsAndCommon = wordDistributionsByIdAndCommonDist(data)

    rankings["wordCount"] = rankWith(
        distributionsAndCommon,
        lambda word, dist, _: dist[word],
    )

    rankings["relativeWordCount"] = rankWith(
        distributionsAndCommon,
        lambda word, dist, commonDist: dist[word] / commonDist[word],
    )

    rankings["relativeWordCountAndPrevalence"] = rankWith(
        distributionsAndCommon,
        lambda word, dist, commonDist: dist[word] / commonDist[word] * dist[word] / dist.N(),
    )

    rankings["relativeWordCountAndPrevalenceMagnitude"] = rankWith(
        distributionsAndCommon,
        lambda word, dist, commonDist: dist[word] / commonDist[word] * log(dist[word]) / log(dist.N()),
    )
    
    rankings["relativeWordCountAndPrevalenceMagnitudeAndSingled"] = rankWith(
        distributionsAndCommon,
        lambda word, dist, commonDist: dist[word] / (commonDist[word] - dist[word] + 1) * log(dist[word]) / log(dist.N()),
    )

    rankings["relativeSingledWordPrevalenceMagintude"] = rankWith(
        distributionsAndCommon,
        lambda word, dist, commonDist: log(dist[word] + 2) / log(commonDist[word] - dist[word] + 2),
    )
    
    rankings["relativeWordCountAndPrevalenceTrial"] = rankWith(
        distributionsAndCommon,
        lambda word, dist, commonDist: dist[word] / commonDist[word] * log(dist[word]/dist.N()),
    )

    stemmedDistributionsAndCommon = stemmedWordDistributionsByIdAndCommonDist(data)

    rankings["relativeStemmedWordCountAndPrevalenceMagnitude"] = rankWith(
        stemmedDistributionsAndCommon,
        lambda word, dist, commonDist: dist[word] / commonDist[word] * log(dist[word]) / log(dist.N()),
    )

    rankings["relativeStemmedWordCountAndPrevalenceMagnitudeAndSingled"] = rankWith(
        stemmedDistributionsAndCommon,
        lambda word, dist, commonDist: dist[word] / (commonDist[word] - dist[word] + 1) * log(dist[word]) / log(dist.N()),
    )
    
    rankings["relativeSingledStemmedWordPrevalenceMagintude"] = rankWith(
        stemmedDistributionsAndCommon,
        lambda word, dist, commonDist: log(dist[word] + 2) / log(commonDist[word] - dist[word] + 2),
    )

    return rankings

# Das ist ein wenig nerfig bei python, wenn man von einem anderen file importiert
#  wird alles in dem file ausgeführt.
#
# Diese aufrage vermeidet das, der __name__ ist eine variable die pro file gesetzt wird, 
# und nur auf __main__ ist wenn dies das original gestartete file ist.
# Um das ein wenig in die bekannte form mit einer main funktion zu bringen ist es üblich
# eine solche zu definieren und hier aufzurufen, wie ich hier getan habe
if __name__ == "__main__":
    main()