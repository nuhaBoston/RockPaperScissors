#when playing RPS the computer needs to randomly throw out a hand
#therefore this should be pretty easy to make the computer play something
#
import random  

#b can either be true or false
def computerPlay(b):
    num = random.randint(1,3)
    if b:
        return num 


def humanPlay(c):
    if c == 1:
        return 1
    if c == 2:
        return 2
    if c == 3:
        return 3
    else:
        return 'You have played an invalid move. Try Again'

## paper covers rock, scissors beats paper, rock beats scissors
def whoWins(b,c):
    if b == 1 and c == 2:
        return 'You won!'
    if b == 2 and c == 1:
        return 'Computer Won!'
    if b == 2 and c == 3:
        return 'You won!'
    if b == 3 and c == 2:
        return 'Computer Won!'
    if b == 1 and c == 3:
        return 'Computer Won!'
    if b == 3 and c == 1:
        return 'You won!'
    if (b == 1 and c == 1) or (b == 2 and c == 2) or (b==3 and c==3):
        return "It's is a tie"

def Game(d):
    print("Welcome to Rock, Paper, Scissors!\n")
    print("You have the choice to play Rock, Paper, or Scissors\n")
    print("Please Type in 1 for Rock, 2 for Paper, 3 for Paper\n")
    playAgain = True
    while(playAgain):
        HumanMove = int(input("What's Your Move?\n"))
        if HumanMove != 1 or HumanMove != 2 or HumanMove != 3:
            print('You have played an invalid move.\n')
            HumanMove = int(input("Try Again: "))
        print(whoWins(humanPlay(HumanMove),computerPlay(HumanMove)))
        yesOrNo = input("\nWould you like to play again? Please reply yes or no \n")
        if yesOrNo == 'yes': 
            playAgain = True
        if yesOrNo == 'no':
            playAgain = False

    return None

Game(1)
