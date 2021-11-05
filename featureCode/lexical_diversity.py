import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def lexicalDiversity(input: str):
    "calculate lexical diversity"
    
    #convert to lowercase
    # input=input.lower
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


# res=lexicalDiversity("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.")
# res2=lexicalDiversity("Affe Esel Ente")
# print(res)
# print(res2)



