from random import randint
def random_noun():
    nouns = ['llama', 'couch']
    return nouns[randint(0,1)]

def random_verb():
    verbs = ['run', 'kayak']
    return verbs[randint(0,1)]


print random_noun()
print random_verb()

# The following is the early Udacity version
# Write code for the function word_transformer, which takes in a string word as input.
# If word is equal to "NOUN", return a random noun, if word is equal to "VERB",
# return a random verb, else return the first character of word.

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"

def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == 'NOUN':
        return random_noun()
    elif word == 'VERB':
        return random_verb()
    else:
        return word[0]

print word_transformer('NOUN')
print word_transformer('VERB')
print word_transformer('42')


# And here's a later version of the Udacity quiz code with my solution
# Let's put it all together. Write code for the function process_madlib, which takes in
# a string "madlib" and returns the string "processed", where each instance of
# "NOUN" is replaced with a random noun and each instance of "VERB" is
# replaced with a random verb. You're free to change what the random functions
# return as verbs or nouns for your own fun, but for submissions keep the code the way it is!

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"

def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    elif word == "VERB":
        return random_verb()
    else:
        return word[0]

def process_madlib(mad_lib):
    processed = ""
    # your code here
    # you may find the built-in len function useful for this quiz
    # documentation: https://docs.python.org/2/library/functions.html#len
    while mad_lib.find('NOUN') != -1:
        mad_lib = mad_lib.replace('NOUN', random_noun(), 1)
        #Udacity would prefer use of the word_transformer fucnction
    while mad_lib.find('VERB') != -1:
        mad_lib = mad_lib.replace('VERB', random_verb(), 1)
        #print mad_lib
    processed = mad_lib
    return processed


test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib(test_string_1)
print process_madlib(test_string_2)
#test = test_string_1.replace('NOUN', random_noun())
#print test
