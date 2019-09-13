#when playing RPS the computer needs to randomly throw out a hand
#therefore this should be pretty easy to make the computer play something
#
import random  

def possiblePlays(a):
    A = []
    if a == 3:
         A = ['rock', 'paper', 'scissors']
    if a == 2:
        A = ['rock', 'paper']
    elif a == 1:
        A = ['rock']
    return A

print(possiblePlays(3))

#b can either be true or false
def computerPlay(b):
    num = random.randint(1,3)
    if b:
        if num == 1:
            return 'rock'
        if num == 2:
            return 'paper'
        if num == 3:
            return 'scissors'

def humanPlay(c):
    

    



