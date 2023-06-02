# This is the word cloud generating alforithms!

# The code is not optimized. Don't judge too hard!!!

# Current problems of the code:
#   1) One pattern is repeated multiple times in the parseString function.
#      I haven't already figured out how the passed dictionary can be accessed (by reference),
#      but not copying it to the function and then returning a new one.
#   2) Also, collecting the excluded words was quite hard. There were some thoughts about
#      how it can be acomplished, but they are not released in this current version of the project. 

import string

# The list of excluded words was created manually

excluded_words = ["Am", "am", "Is", "is", "Are", "are", "em", "Em", "'em", "'Em", ".", ",", "!", ":", ";", "The", "the", "and", "And", "A", "a", "or", "Or", "I", "i", "my", "My", "im",
                  "Im", "You", "you", "me", "Me", "Yeah", "yeah", "in", "In", "up", "Up", "this", "This", "they", "They", "that", "That", "it", "It", "got", "Got", "from", "From", "with",
                  "With", "to", "To", "on", "On", "do", "Do", "dont", "Dont", "for", "For", "Of", "of", "its", "Its", "we", "We", "aint", "Aint", "when", "When", "No", "no", "be", "Be",
                  "what", "What", "thats", "Thats", "go", "Go", "oh", "Oh", "so", "So", "been", "Been", "out", "Out", "take", "Take", "not", "Not", "Now", "now", "all", "All", "nah", "Nah",
                  "she", "She", "cant", "Cant", "cause", "Cause", "but", "But", "these", "These", "those", "Those", "was", "Was", "Were", "were"]

# This function parses through the given string (str) 
# and returns the number of occurances of each word

def parseString(str):
    occurs = {}
    tmp_str = ""
    for i in range(len(str)):
        if str[i] == ' ':
            if tmp_str in occurs.keys():
                occurs[tmp_str] += 1
                tmp_str = ""
                continue
            else:
                occurs[tmp_str] = 1
                tmp_str = ""
                continue
        if str[i] == '\r':
            if tmp_str in occurs.keys():
                occurs[tmp_str] += 1
                tmp_str = ""
                continue
            else:
                occurs[tmp_str] = 1
                tmp_str = ""
                continue
        if str[i] == '\n':
            tmp_str = ""
            continue
        if str[i] in string.punctuation:
            continue
        tmp_str += str[i].lower()
        if i == len(str) - 1:
            if tmp_str in occurs.keys():
                occurs[tmp_str] += 1
                tmp_str = ""
                continue
            else:
                occurs[tmp_str] = 1
                tmp_str = ""
                continue
    return occurs

# This function deletes the excluded words and 
# returns "clean" dictionary

def deleteExcludedWords(occurs):
    clean = {}
    for i in occurs.keys():
        if i in excluded_words:
            continue
        else:
            clean[i] = occurs[i]
    return clean

# This function gets the first 20 values since the word cloud will be generated 
# only with 20 words. Not less and not more.

def getFirst20Values(clean):
    weights = {}
    srt = sorted(clean.items(),key = lambda dc: dc[1], reverse = True)
    for i in range(20):
        weights[srt[i][0]] = srt[i][1]
    return weights

# This is the actual function that is being used in the Flask Apricity application to return
# prepared dictionary for generating a word cloud

def Word_Cloud(dict):
    str = ""
    str += dict["lyrics1"]
    str += dict["lyrics2"]
    str += dict["lyrics3"]
    str += dict["lyrics4"]
    str += dict["lyrics5"]
    D = getFirst20Values(deleteExcludedWords(parseString(list(str))))
    n = 20
    final = {}
    for i in D.keys():
        while n != 0:
            final[n] = i
            n -= 1
            break
    return final

