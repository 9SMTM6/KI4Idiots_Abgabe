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
        input_name: str = "20newsgroups",
    ):
        # This is the constructor of classes in Python
        self.input_name = input_name

        self.input_path: str = f"{input_name}.json"
        # if no string was passed generate one from the input path

        # Internal methods, that get called by python, as the constructor is one, get framed in 2 underscores
        with open(self.input_path) as filePointer:
            # these types are simply suggestions to get better code completion, and not required.
            self.jsonRepr: dict = json.load(filePointer)
        # self.header = jsonRepr["header"]
        # sparse and weight hold no value, theyre constantly false, 1.0, so we skip them
        data: list[dict] = [entry["values"] for entry in self.jsonRepr["data"]]
        self.blogEntries: list[str] = []
        self.blogEntriesById = {str(group): [] for group in range(4)}
        # self.ids: list[str] = []
        # self.groups: list[str] = []
        for id, blogEntry, group in data:
            self.blogEntriesById[group].append(blogEntry)
            # self.ids.append(id)
            self.blogEntries.append(blogEntry)
            # self.groups.append(group)

    def addData(self, additionalData: dict[str, list[float]], keepText = False):
        """
        Add the passed data to the internal representation, in a format Weka can read
        """
        # In methods, as with the constructor, you need to explicitly pass the class instance, 
        # called self instead of this, in the parameter list.

        # A static method simply doesnt have a self parameter.
        attributesHeader: list = self.jsonRepr["header"]["attributes"]
        (groupHeader, attributesHeader) = removeIdTextAndCutGroup(attributesHeader, False)
        for featureName, _ in additionalData.items():
            attributesHeader.append({
                "name": featureName,
                "type": "numeric",
                "class": False,
                "weight": 1.0,
            })
        blogEntryValues: list = self.jsonRepr["data"]
        for idx, blog in enumerate(blogEntryValues):
            blogValues:list = blog["values"]
            (group, blogValues) = removeIdTextAndCutGroup(blogValues, keepText)
            for _, featureValues in additionalData.items():
                # need to convert to string because weka doesnt like the value 0.0 as float
                blogValues.append(str(featureValues[idx]))
            blogValues.append(group)
            blog["values"] = blogValues
        attributesHeader.append(groupHeader)
        self.jsonRepr["header"]["attributes"] = attributesHeader
        return self

    def saveToFile(self, specificOutputPath = None):
        """
        Save the internal representation to a json file
        """
        specificOutputPath: str = specificOutputPath or f"{self.input_name}_processed"

        with open(f"{specificOutputPath}.json", "w") as filePointer:
            json.dump(self.jsonRepr, filePointer, indent=4)

def removeIdTextAndCutGroup(input: list, keepText: bool):
    [id, text, group, *remainder] = input
    if keepText:
        output = [text, *remainder]
    else:
        output = remainder
    return (group, output)
