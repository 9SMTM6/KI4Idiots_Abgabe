from nltk.tokenize import word_tokenize

def clean_up_punctuation(tokens):
    "throw out all tokens only made of non-alphanumeric chars"
    tokens_cleaned=[]

    for t in tokens:

        is_all_punct=True
        for ch in t:
            if(ch.isalnum()):
                is_all_punct=False
        if(not is_all_punct):
            tokens_cleaned.append(t)
    return tokens_cleaned


def total_word_count(input: str):
    "count all words in post disregarding punctuation"
    return len(clean_up_punctuation(word_tokenize(input)))
