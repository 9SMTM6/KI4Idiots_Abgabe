from nltk.tokenize import sent_tokenize

from featureCode.total_word_count import total_word_count

def avg_sentence_length(input:str):
    "# The average sentence length directly as return value"
    avg_sent_box = sent_tokenize(input)
    return total_word_count(input)/len(avg_sent_box)
    
        



# print(avg_sent_box)


#avg_sentence_length("Hallo, dies ist einen blöder Test. Der Test dient dazu um blöde Methoden in Python zu testen. War der Test erfolgreich?")


    