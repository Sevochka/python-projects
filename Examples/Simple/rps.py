import random
import sys

# These variables keep track of the number of wins, losses, and ties. wins = 0 losses = 0 ties = 0
wins = 0
losses = 0
ties = 0

possibleMoves = ['r', 'p', 's']
rules = {
    'r': {'win': 's', 'lose': 'p'},
    'p': {'win': 'r', 'lose': 's'},
    's': {'win': 'p', 'lose': 'r'},
}


def check(actualMove, generatedMove):
    global ties, wins, losses
    if generatedMove == actualMove:
        print('It is a tie')
        ties += 1
    else:
        if generatedMove == rules[actualMove]['win']:
            print("You win")
            wins += 1
        else:
            print("You lose")
            losses += 1


while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        move = input()
        if move == 'q':
            sys.exit()
        if move in possibleMoves:
            break

    print(move + ' versus...')
    randomNum = random.randint(0, 2)
    print(possibleMoves[randomNum])
    check(move, possibleMoves[randomNum])
