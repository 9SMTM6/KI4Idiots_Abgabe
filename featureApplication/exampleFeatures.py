"""Some, probably not interesting for the future, feature functions that I used to test
"""

def countAsciiValues(input: str):
    return sum([ord(char) for char in list(input)])

def getLength(input: str):
    return len(input)
