import json

def loadData():
    with open("20newsgroups.json") as filePointer:
        data: dict = json.load(filePointer)
        header = data["header"]
        data: list[dict] = data["data"]
        pureData: list[str] = [entry["values"][1] for entry in data]
        return pureData