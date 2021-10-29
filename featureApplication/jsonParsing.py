"""
This handles the reading from the JSON file,
and saving the results of the application of our feature functions to another JSON file
"""
import json

class JsonData:
    """Lets see if our PCs blow up due to the RAM hunger this might have"""

    # Python has no concept of private and public,
    # if something is meant to be "private" its convention to prepend an underscore to it.
    # BEWARE: Variables assigned here are STATIC variables
    _SOME_STATIC_VAR = "whatever"

    def __init__(
        self, 
        input_path:str = "20newsgroups", 
        specific_output_path = None,
    ):
        # This is the constructor of classes in Python

        self.input_path: str = f"{input_path}.json"
        # if no string was passed generate one from the input path
        self.specific_output_path: str = specific_output_path or f"{input_path}_processed.json"

        # Internal methods, that get called by python, as the constructor is one, get framed in 2 underscores
        with open(self.input_path) as filePointer:
            # these types are simply suggestions to get better code completion, and not required.
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

    def saveToFile(self, additionalData: dict[str, list[float]]):
        # In methods, as with the constructor, you need to explicitly pass the class instance, 
        # called self instead of this, in the parameter list.
        
        # A static method simply doesnt have a self parameter.
        with open(self.specific_output_path, "w") as filePointer:
            for key, data in additionalData.items():
                self.jsonRepr["header"]["attributes"].append({
                    "name": key,
                    "type": "numeric",
                    "class": False,
                    "weight": 1.0,
                })
                for idx, entry in enumerate(data):
                    self.jsonRepr["data"][idx]["values"].append(entry)
            json.dump(self.jsonRepr, filePointer, indent=4)
