#define all functions to generate features here
#every function needs 2 arguments: text -> post text
#                                   search_param -> additional parameter to use in function,
#                                                   necessary even if not used

def countSpecificWord(text, search_param):
    "count occurences of a specific word in a post"
    return text.count(search_param)

def countWords(text,search_param):
    "count number of words in a post"
    return len(text)

def return_post(text,search_param):
    "return post with quotes around it"
    return f"\"{text}\""