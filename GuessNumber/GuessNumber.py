import random
import simplegui

secretNum = 0
NumRange = 100
GuessesLeft = 7



# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secretNum, Numrange, GuessesLeft
    secretNum = random.randrange(0, NumRange)
    if NumRange == 100:
        GuessesLeft = 7
    if NumRange == 1000:
        GuessesLeft = 10
    print(f"\nNew Game. Range is 0 to {NumRange}.")
    print(f"Number of remaining guesses is {GuessesLeft}.")
    #Debugging Code
    #print(secretNum)

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global NumRange, GuessesLeft
    NumRange = 100
    GuessesLeft = 7
    new_game()
   

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global NumRange, GuessesLeft
    NumRange = 1000
    GuessesLeft = 10
    new_game()
   
    
def input_guess(guess):
    # main game logic goes here	
    global GuessesLeft
    guess = int(guess)
    if GuessesLeft == 7 or GuessesLeft == 10:
        GuessesLeft -= 1
    if GuessesLeft > 0:
        if guess > secretNum:
            print(f"Higher. Guesses Remaining: {GuessesLeft}.")
            GuessesLeft -= 1
        elif guess < secretNum:
            print(f"Lower. Guesses Remaining: {GuessesLeft}.")
            GuessesLeft -= 1
        else:
            print("Got it!")
            new_game()
    else: 
        print(f"Out of Guesses. Correct Answer was {secretNum}. Game Over.")
        new_game()
            
  
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess:", input_guess, 200)


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
