import random
import json

class RandomSplit:
    def __init__(self, jsonRepr: dict):
        # set random state to ensure reproducibility
        random.seed(len("KI4Idiots"))

        header = jsonRepr["header"]
        data: list = jsonRepr["data"]
        # randomly shuffle the date for later random selection
        random.shuffle(data)
        train_until = int(0.8 * len(data))
        compare_until = int(0.9 * len(data))
        # split the shuffled data in designated data sets with an 80:10:10 rule
        self.train = {
            "header": header,
            "data": data[:train_until],
        }
        self.compare = {
            "header": header,
            "data": data[train_until: compare_until],
        }
        self.validate = {
            "header" : header,
            "data": data[compare_until:],
        }

    def saveToFiles(self, startName: str):
        for name in ["train", "compare", "validate"]:
            with open(f"./{startName}_{name}.json", "w") as filePointer:
                json.dump(self.__dict__[name], filePointer, indent=4)
