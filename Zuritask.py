import random
game = ['R','P','S']
useropt = 'R'
compopt = 'R'
while (useropt ==compopt):
    print()
    print('Rock-Paper-Scissors')
    print()
    print('Use the following input methods for selection')
    print('input R for Rock')
    print('input P for Paper')
    print('input S for Scissors')
    print()

    useropt = input('pick a game option: ')
    useropt = useropt.upper()

    if useropt in game:

        compopt = random.choice(game)

        if (compopt=='R' and useropt=='S'):
            print("Computer Wins")

        elif (compopt=='P' and useropt=='R'):
                print("Computer Wins")

        elif (compopt=='S' and useropt=='P'):
                print("Computer Wins")

        elif (compopt == useropt):
            print("TIE")

        else:
            print("YOU WIN")

    else:
            useropt = 'R'
            print ("Invalid input")
            print ("Pick a Valid Selection")

else:
            print ("Thank you for playing")
    
