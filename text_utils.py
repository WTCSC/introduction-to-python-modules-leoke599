def count_chars(text):
    chars = len(list(text)) # splits the file into a list and counts all of them
    return chars
    

def count_words(text):
    words = len(text.split()) # splits the text by any whitespace and counts them
    return words

def count_sentences(text):
    import re
    sent = [x for x in re.split("[.|!|?]", text) if x!=""] # i found this online and im not 100% sure about what everything does but i know the re.split splits the text into whatever the first argument is. the | is like an or statement and the second argument is the thing that needs to be split. the if x!="" is used to ignores empty characters
    return len(sent)