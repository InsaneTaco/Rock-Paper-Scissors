while True:
    import random
    move = input('Welcome to Epic Rock Paper Scissors! Make your move. Type your move in all lowercase. ')
    oppnumber = random.randint(1,3)
    if oppnumber == 1:
        oppmove = 'rock'
    elif oppnumber == 2:
        oppmove = 'paper'
    elif oppnumber == 3:
        oppmove = 'scissors'
    if move == 'rock' and oppmove == 'rock':
        print('Opponent chose rock. Draw.')
    elif move == 'rock' and oppmove == 'scissors':
        print('Opponent chose scissors. You won!')
    elif move == 'rock' and oppmove == 'paper':
        print('Opponent chose paper. Defeat.')
    elif move == 'paper' and oppmove == 'paper':
        print('Opponent chose paper. Draw.')
    elif move == 'paper' and oppmove == 'rock':
        print('Opponent chose rock. You won!')
    elif move == 'paper' and oppmove == 'scissors':
        print('Opponent chose scissors. Defeat.')
    elif move == 'scissors' and oppmove == 'scissors':
        print('Opponent chose scissors. Draw.')
    elif move == 'scissors' and oppmove == 'paper':
        print('Opponent chose paper. You won!')
    elif move == 'scissors' and oppmove == 'rock':
        print('Opponent chose rock. Defeat.')
