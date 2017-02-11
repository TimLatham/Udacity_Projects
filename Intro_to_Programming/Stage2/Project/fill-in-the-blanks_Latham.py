# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

import random # so that a random flashcard can be chosen for each iteration

# find blanks in a provided sentence given a list of potential blanks to fill
def findBlanks(sentence, blanks1):
    for i in blanks1:
        if sentence.find(i) > -1:
            blanksInString.append(i)

# choose a random item from a list of sentences            
def grabSentence(sentenceList):
    randomItem = random.randint(1, len(sentenceList))
    sentence = sentenceList[randomItem-1]
    return sentence

# Take user input to replace blank items in the flashcard.
def flashMe(sentence):
    output = sentence
    for i in blanksInString:
        user_input = raw_input("Type in a: " + i + " ")
        output = output.replace(i, user_input)
    return output

# The fill in the blanks sentences used as flash cards
comment = '''A ___1___ is created by using the # symbol.  You should add ___1___s to describe how the overall
___2___ works, as well as for each defined ___3___.  This will add clarity to your code for when you return
to it or someone else is debugging it.'''

loops = '''There are two main kinds of ___1___s in Python.  The first is a ___2___ ___1___, which iterates a 
specified number of times. The second is a ___3___ ___1___, which will iterate as long as the condition remains
True.  ___2___ ___1___s are a simplified case of ___3___ ___1___s.'''

boolean = '''A ___1___ is an item that can be one thing or the other, either ___2___ or ___3___.  If a 
condition is ___2___, it is in accordance with fact or reality.  If a condition is ___3___, it is not.'''

megaMem = '''My Very Educated Mother Just Served Us Nine Pizzas is a popular mnemonic device.  It is
a good way to remember that ___1___, ___2___, ___3___, ___4___, ___5___, ___6___, ___7___, ___8___ and 
___9___ are the 9 planets.  Yes, I don't care what they say, ___9___ is a planet.  If ___1___ counts, 
then certainly ___9___ counts.'''


# A list of potential replacement blanks to be passed in to the flashMe function. 
blanks1  = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___", "___7___", "___8___", "___9___"]

# Put the flashCards into a list so that grabSentence can be invoked to pick a randome item at runtime
flashCards = [sample, comment, loops, boolean, megaMem]
sentence = grabSentence(flashCards)
print sentence

# For the randomly chosen flashcard, identify which blanks are used and load into a list
blanksInString = []
findBlanks(sentence, blanks1)

# For the randomly generated sentence, replace the identified blanks with user input
print flashMe(sentence)