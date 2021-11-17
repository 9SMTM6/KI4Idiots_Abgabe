import re

def contains_bible_reference_bool(input: str):
    '''
    Search for bible references in passed string.

    PARAMETERS
        input:str
            String to be searched

    RETURNS
        true   in case of found something
        false  otherwise
    '''
    pattern = "(?:\d|I{1,3})?\s?\w{2,}\.?\s*\d{1,}\:\d{1,}-?,?\d{0,2}(?:,\d{0,2}){0,2}"
    if re.search(pattern, input):
        return 1
    else:
        return 0

def contains_bible_reference_number(input: str):
    '''
    Search for bible references in passed string.

    PARAMETERS
        input:str
            String to be searched

    RETURNS
        int,    number of occurences
    '''
    pattern = "(?:\d|I{1,3})?\s?\w{2,}\.?\s*\d{1,}\:\d{1,}-?,?\d{0,2}(?:,\d{0,2}){0,2}"
    return len(re.findall(pattern, input))
