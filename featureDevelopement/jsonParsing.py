import json

class JsonData:
    """Lets see if our PCs blow up due to the RAM hunger this might have"""
    def __init__(self):
        with open("./20newsgroups.json",) as filePointer:
            self.jsonRepr: dict = json.load(filePointer)
            # self.header = jsonRepr["header"]
            # sparse and weight hold no value, theyre constantly false, 1.0, so we skip them
            data: list[dict] = [entry["values"] for entry in self.jsonRepr["data"]]
            self.blogEntries: list[str] = []
            # self.ids: list[str] = []
            # self.groups: list[str] = []
            for id, blogEntry, group in data:
                # self.ids.append(id)
                self.blogEntries.append(blogEntry)
                # self.groups.append(group)

    def saveToFile(self, additionalData: dict[list[float]]):
        with open("./processedData.json", "w") as filePointer:
            for key, data in additionalData.items():
                self.jsonRepr["header"]["attributes"].append({
                    "name": key,
                    "type": "numeric",
                    "class": False,
                    "weight": 1.0,
                })
                for idx, entry in enumerate(data):
                    self.jsonRepr["data"][idx]["values"].append(entry)
            json.dump(self.jsonRepr, filePointer)
