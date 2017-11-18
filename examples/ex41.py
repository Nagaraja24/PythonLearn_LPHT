import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
     "Make a class named %%% that is-a %%%.",
    "class %%%(object): \n\tdef __init__(self, ***)" :
     "clas %%% has-a function that takes self and *** parameters."
    "*** = %%%()"
     "Set *** to an instance of class %%%.",
    "***.***(@@@)":
     "From *** get the *** function and call it with self and @@@ parameters",
    "***.*** = '***'":
     "From *** get the *** attribute and set it it '***' ",

}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] =="english":
    PHRASE_FIRST = True

#load up the words from website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

def convert(snippet, phrases):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []
    


    
    
    
