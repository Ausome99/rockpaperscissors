import random


choices = [
    'rock',
    'paper',
    'scissors'
]

wins = 0
losses = 0
ties = 0

print('Rock, Paper, Scissors or Stop?\n')

player = input()
player = player.lower()
    
if player == 'rock' or 'paper' or 'scissors':
    choice = random.choice(choices)
    print(f"I chose {choice}")

    if choice == 'rock' and player == 'paper':
        print('YOU WON!!!')
        wins += 1
    elif choice == 'paper' and player == 'scissors':
        print('YOU WON!!!')
        wins += 1
    elif choice == 'scissors' and player == 'rock':
        print('YOU WON!!!')
        wins += 1
    elif choice == 'rock' and player == 'scissors':
        print('YOU LOST...')
        losses += 1
    elif choice == 'paper' and player == 'rock':
        print('YOU LOST...')
        losses += 1
    elif choice == 'scissors' and player == 'paper':
        print('YOU LOST...')
        losses += 1
    elif choice == 'rock' and player == 'rock':
        print('YOU TIED.')
        ties += 1
    elif choice == 'paper' and player == 'paper':
        print('YOU TIED.')
        ties += 1
    elif choice == 'scissors' and player == 'scissors':
        print('YOU TIED.')
        ties += 1
elif player == 'stop':
    print(f"You won {wins} times and lost {losses} times and tied {ties} times")
    break
    