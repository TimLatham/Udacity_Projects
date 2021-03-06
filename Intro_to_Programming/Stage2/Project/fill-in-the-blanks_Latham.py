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



def startGame():
    """
    Behavior:   This function resets items and begins each new game
    Inputs:     Takes no inputs
    Outputs:    Generates the inputs needed and outputs to the mainLoop function
    """
    chosenLevel = chooseLevel()
    loadLevel = levelsShort.index(chosenLevel)
    maxGuesses = numberGuesses()
    findBlanks(levels[loadLevel], blanks1)
    mainLoop(levels[loadLevel], loadLevel, maxGuesses)

def chooseLevel():
    """
    Behavior:   Allow user to select difficulty level, including a hidden easter egg level and the sample level
    Inputs:     Takes no inputs
    Outputs:    Returns the first character of the string assigned to level
    """
    print "Please select a game difficuly by typing it in"
    print "possible choices include easy, medium and hard"
    level = raw_input().lower()
    while level not in POSSIBLELEVELS:
        print
        print "Acceptable input is e, easy, m, medium, h, or hard"
        print
        level = raw_input().lower()
    print "You've chosen: " + level + '!!'
    return level[FIRSTITEM]
  
def numberGuesses():
    """
    Behavior:   This function allows the user to define the maximum incorrect guesses
                they can enter, in a range from 1 to 10
    Inputs:     Takes no inputs
    Outputs:    Returns the maximum guesses selected by the user as an integer
    """
    print "Please choose the maximum incorrect guesses (1-10)"
    maxGuesses = raw_input()
    if not maxGuesses.isdigit():
        print "Please enter a NUMBER from 1 to 10"
        print
        numberGuesses()
    elif not int(maxGuesses) in range(1,11):
        print "Please enter a number from 1 to 10"
        print
        numberGuesses()
    else:
        print 'You will get: ' + maxGuesses + ' guesses per problem.'
        print
        return int(maxGuesses)
    
def findBlanks(fillIn, blanks1):
    """
    Behavior:   Find blanks in a provided sentence(s) given a list of potential blanks to fill
    Inputs:     fillIn, which is the paragraph for the selected level, and blanks1
                which is a list of potential blanks
    Outputs:    None, but populates the list blanksInString with the blanks that are in 
                the selected levels paragraph
    """
    for item in blanks1:
        if fillIn.find(item) > -1:
            blanksInString.append(item)

def mainLoop(level, loadLevel, maxGuesses):
    """
    Behavior:   This is the main game loop which controls overall play
    Inputs:     level, which is the paragraph corresponding to the level selected by the user
                loadLevel, which is the item in the levels list corresponding to level
                maxGuesses, which is the maximum potential incorrect items per user selection
    Outputs:    The game behavior for user interaction of guessing and completing the paragraph
    """
    currentParagraph = level
    remainingGuesses = maxGuesses
    questionNumber = 1
    while len(blanksInString) > 0 and remainingGuesses > 0:
        subloop(remainingGuesses, currentParagraph)
        guess = raw_input().lower()
        if guessCheck(guess, loadLevel, questionNumber) == True:
            currentParagraph = updateParagraph(currentParagraph, guess)
            questionNumber += 1
            remainingGuesses = maxGuesses
        else:
            print guess + ' is not correct!'
            remainingGuesses -= 1
            if remainingGuesses == 0:
                print 'You have run out of guesses!'
    print 'GAME OVER'
    
def subloop(remainingGuesses, currentParagraph):
    """
    Behavior:   Lets user know the guesses remaining, current paragraph state, and asks for the next input
    Inputs:     remainingGuesses, the count of incorrect guesses possible before losing,
                currentParagraph, the current paragraph state for the selected level
    Outputs:    None, but provides onscreen user feedback
    """
    print 'You have: ' + str(remainingGuesses) + ' guesses remaining.'
    print 'The current paragraph reads as such:'
    print currentParagraph
    print 'What should be substituted for ' + blanksInString[FIRSTITEM] + '?'


def guessCheck(guess, loadLevel, questionNumber):
    """
    Behavior:   Checks the user's guess versus the solution key and updates for correct answers
    Inputs:     guess, the users input for the currently considered item
                loadLevel, which is the item in the levels list corresponding to level
                questionNumber, the current item being reviewed out of potential blank items
    Outputs:    Returns True if the guess is correct, otherwise False
    """
    if guess == answers[loadLevel][questionNumber-1]:
        print 'Correct!'
        print
        return True
    return False

def updateParagraph(currentParagraph, guess):
    """
    Behavior:   This function updates the fill in the blank for guesses that are correct
    Inputs:     currentParagraph, which is the paragraph as it currently stands
                guess, the users input for the currently considered item
    Outputs:    Returns currentParagraph after updating it with the correct user guess for the currently
                considered item, unless the entire paragraph has been correctly completed, which
                will move the user to the endGame function
    """
    currentParagraph = currentParagraph.replace(blanksInString[FIRSTITEM], guess.upper())
    blanksInString.remove(blanksInString[FIRSTITEM])
    if completeCheck() == True:
        endGame(currentParagraph)
    else:
        return currentParagraph

def completeCheck():
    """
    Behavior:   This function checks if the fill in the blank has been completed
    Inputs:     Takes no inputs
    Outputs:    Returns True is the puzzle is completed, indicated by no items left in 
                the blanksInString list, otherwise returns False
    """
    if len(blanksInString) == 0:
        return True
    return False


def endGame(currentParagraph):
    """
    Behavior:   This function closes out a winning game
    Inputs:     currentParagraph, which in this case is the completed/solved version
    Outputs:    Screen production of winning message and the completed paragraph
    """
    print
    print 'YOU WON!!!!!!!!'
    print
    print 'The solution is:'
    print (currentParagraph)
    print

# all caps for indicating a variable that never changes aka a constant
POSSIBLELEVELS = ['easy', 'medium', 'hard', 'e', 'm', 'h', 'impossible', 'i', 'sample', 's']

# Text for each of the levels
easy = '''A ___1___ is created by using the # symbol.  You should add ___1___s to describe how the overall
___2___ works, as well as for each defined ___3___.  This will add clarity to your code for when you return
to it or someone else is debugging it.  To make multi-line ___1___s or paragraphs, use three ___4___ marks'''

medium = '''There are two main kinds of ___1___s in ___4___.  The first is a ___2___ ___1___, which iterates a 
specified number of times. The second is a ___3___ ___1___, which will iterate as long as the condition remains
True.  ___2___ ___1___s can be used as a streamlined case of ___3___ ___1___s.'''

hard = '''A ___1___ is an item that can be one thing or the other, either ___2___ or ___3___.  If a 
condition is ___2___, it is in accordance with fact or reality.  If a condition is ___3___, it is not.  ___4___ 
operators, such as 'and' and '___5___' are frequently used in conjunction with ___1___s.'''

impossible = '''My Very Educated Mother Just Served Us Nine Pizzas is a popular mnemonic device.  It is
a good way to remember that ___1___, ___2___, ___3___, ___4___, ___5___, ___6___, ___7___, ___8___ and 
___9___ are the 9 planets.  Yes, I don't care what they say, ___9___ is a planet.  If ___1___ counts, 
then certainly ___9___ counts.'''

levels = [easy, medium, hard, impossible, sample]
levelsShort = ['e', 'm', 'h', 'i', 's']

# Solutions list for each problem set
easyAnswer = ['comment', 'program', 'function', 'quotation']
mediumAnswer = ['loop', 'for', 'while', 'python']
hardAnswer = ['boolean', 'true', 'false', 'logical', 'or']
impossibleAnswer = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
sampleAnswer = ['function', 'arguments', 'none', 'list']

answers = [easyAnswer, mediumAnswer, hardAnswer, impossibleAnswer, sampleAnswer]

# A list of potential replacement blanks to be passed in to the mainLoop function. 
blanks1  = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___", "___7___", "___8___", "___9___"]
# Python starts counting at zero, therefore the first item in a string or list is item 0
# Adding this per Udacity reviewer feedback to avoid "magic numbers"
# all caps for indicating a variable that never changes aka a constant
FIRSTITEM = 0

# Code that plays the game
blanksInString = []
startGame()