import nltk
from nltk.tokenize import word_tokenize

def lexicalDiversity(input: str):
    #prepare input with stemmer (Wortstämme herausfinden)
    porter_stemmer=nltk.PorterStemmer()
    input_token=word_tokenize(input)
    input_token=[porter_stemmer.stem(t) for t in input_token]

    #result is number of different words divided by total wordcount
    return len(set(input_token))/len(input_token)


# res=lexicalDiversity("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.")
# res2=lexicalDiversity("Affe Esel Ente")
# print(res)
# print(res2)



