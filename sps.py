import random

t = ["stone", "paper", "scissor" ]

play = 'y'
while play == 'y':
    computer = random.choice(t)
    user = input("choose one :stone , paper, scissor? ")
    if user == computer:
        print('DRAW!The computer\' choice was ',computer)
        print("draw, try again")
    elif user == "stone":
        if computer == "paper":
            print('YOU LOSE! The computer\' choice was ',computer)
        else:
            print('NICE! YOU WON! The computer\' choice was ',computer)
    elif user == "paper":
        if computer == 'scissor':
            print('YOU LOSE! The computer\' choice was ',computer)
        else:
            print('NICE! YOU WON! The computer\' choice was ',computer)
    elif user == "scissor":
        if computer == 'stone':
            print('YOU LOSE! The computer\' choice was ',computer)
        else:
            print('NICE! YOU WON! The computer\' choice was ',computer)
    play = input("do you want to play again?y/n:\n")
    play = play.lower()

else:
    print('ok then!')
    
