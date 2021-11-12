from nltk.tokenize import word_tokenize

def clean_up_punctuation(tokens):
    "throw out all tokens only made of non-alphanumeric chars"
    
    tokens_cleaned=[]

    for t in tokens:
        #check if every char is non alphanumeric
        is_all_punct=True
        for ch in t:
            if(ch.isalnum()):
                is_all_punct=False
        #only add if contains alphanumeric char
        if(not is_all_punct):
            tokens_cleaned.append(t)
    return tokens_cleaned


def total_word_count(input: str):
    "count all words in post disregarding punctuation"
    return len(clean_up_punctuation(word_tokenize(input)))

def average_word_length(input: str):
    "calculate average word/token length disregarding punctuation"
    tokens_cleaned=clean_up_punctuation(word_tokenize(input))
    length_sum=0
    token_count=0
    #sum token lengths
    for t in tokens_cleaned:
        length_sum=length_sum+len(t)
        token_count=token_count+1

    #if there are 1 or more tokens calculate average    
    avg=0
    if(token_count!=0):
        avg=length_sum/token_count
    return avg

def max_word_length(input: str):
    "calculate maximum word length, disregarding punctuation"
    tokens_cleaned=clean_up_punctuation(word_tokenize(input))
    max_length=0
    for t in tokens_cleaned:
        l=len(t)
        if(l>max_length):
            max_length=l
    return max_length

