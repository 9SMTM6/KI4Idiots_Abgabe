import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def lexicalDiversity(input: str):
    "calculate lexical diversity"
    
    #convert to lowercase
    # input=input.lower
    #tokenize input
    input_token=word_tokenize(input)

    #result is number of different words divided by total wordcount
    return len(set(input_token))/len(input_token)

def lexicalDiversityNostop(input: str):
    "calculate lexical diversity with whole words and without stopwords"

    #convert to lowercase
    input=input.lower

    #tokenize input
    input_token=word_tokenize(input)

    stop_words=stopwords.words("english")
    #remove stopwords
    input_token_filtered = [w for w in input_token if not w.lower() in stop_words]

    #result is number of different words divided by total wordcount
    return len(set(input_token_filtered))/len(input_token_filtered)

def lexicalDiversityStemmed(input: str):
    "calculate lexical diversity with stemmed words (Porter Stemmer: fast simple) stopwords included"

    #convert to lowercase
    input=input.lower

    #tokenize input
    input_token=word_tokenize(input)

    #prepare input with stemmer (Wortstämme herausfinden)
    porter_stemmer=nltk.PorterStemmer()
    input_token_filtered_stemmed=[porter_stemmer.stem(t) for t in input_token]


    #result is number of different words divided by total wordcount
    return len(set(input_token_filtered_stemmed))/len(input_token_filtered_stemmed)

def lexicalDiversityStemmedNostop(input: str):
    "calculate lexical diversity with stemmed words (Porter Stemmer: fast, simple) and without stopwords"

    #convert to lowercase
    input=input.lower

    #tokenize input
    input_token=word_tokenize(input)

    stop_words=stopwords.words("english")
    #remove stopwords
    input_token_filtered = [w for w in input_token if not w.lower() in stop_words]

    #prepare input with stemmer (Wortstämme herausfinden)
    porter_stemmer=nltk.PorterStemmer()
    input_token_filtered_stemmed=[porter_stemmer.stem(t) for t in input_token_filtered]


    #result is number of different words divided by total wordcount
    return len(set(input_token_filtered_stemmed))/len(input_token_filtered_stemmed)

def lexicalDiversityLemmatized(input: str):
    "calculate lexical diversity with lemmatized words (actual grammatical stem used) stopwords included"

    #convert to lowercase
    input=input.lower

    #tokenize input
    input_token=word_tokenize(input)

    #prepare input with lemmatizer (Wortstämme herausfinden)
    lemmatizer=WordNetLemmatizer
    input_token_lemmatized=[lemmatizer.lemmatize(t) for t in input_token]


    #result is number of different words divided by total wordcount
    return len(set(input_token_lemmatized))/len(input_token_lemmatized)

def lexicalDiversityLemmatizedNostop(input: str):
    "calculate lexical diversity with with lemmatized words (actual grammatical stem used) and without stopwords"

    #convert to lowercase
    input=input.lower

    #tokenize input
    input_token=word_tokenize(input)

    stop_words=stopwords.words("english")
    #remove stopwords
    input_token_filtered = [w for w in input_token if not w.lower() in stop_words]

    #prepare input with lemmatizer (Wortstämme herausfinden)
    lemmatizer=WordNetLemmatizer
    input_token_filtered_lemmatized=[lemmatizer.lemmatize(t) for t in input_token_filtered]

    #result is number of different words divided by total wordcount
    return len(set(input_token_filtered_lemmatized))/len(input_token_filtered_lemmatized)

