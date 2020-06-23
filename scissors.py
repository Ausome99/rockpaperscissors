import random

choices = [
    'rock',
    'paper',
    'scissors'
]

wins = 0
losses = 0
ties = 0

while wins <10 and losses <10:
    print('\nRock, Paper, Scissors or Stop?\n')

    player = input()
    player = player.lower()

    if player == 'stop':
        print(f"You won {wins} times and lost {losses} times and tied {ties} times")
        break

    if player == 'rock' or 'paper' or 'scissors':
        choice = random.choice(choices)

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
            print("")

    print(f"I chose {choice}")
    print(f'You have won {wins} times, lost {losses} times and tied {ties} times')

if wins == 10:
    print(f'\nYou Won!!! Great Job! You won {wins} times, lost {losses} times and tied {ties} times')
elif losses == 10:
    print(f'\nYou lost. Too Bad... You lost {losses} times, won {wins} times and tied {ties} times')

    
