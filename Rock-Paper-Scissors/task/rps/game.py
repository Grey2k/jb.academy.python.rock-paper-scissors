import random

# Write your code here
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

COMMAND_EXIT = '!exit'
COMMAND_RATING = '!rating'

FILE_RATING = 'rating.txt'

SCORE_DRAW = 50
SCORE_WIN = 100

combinations = {ROCK: PAPER, PAPER: SCISSORS, SCISSORS: ROCK}


def is_winner(pick: str, option: str, options: list):
    copy = options[:]

    i = 0
    for item in options:
        if item == pick:
            del copy[i]
            break

        i += 1

    new_list = copy[i:] + copy[:i]

    winners = new_list[:len(new_list) // 2]
    losers = new_list[len(new_list) // 2:]

    if option in winners:
        return False
    elif option in losers:
        return True

    return None


def get_rating(name: str) -> int:
    rating = open(FILE_RATING, 'a+', encoding='utf-8')
    rating.seek(0)

    saved_rating = 0

    for line in rating:
        player, file_rating = line.split()

        if player == name:
            saved_rating = int(file_rating)
            break

    rating.close()
    return saved_rating


# Entrypoint
input_name = input('Enter your name: ')

print(f'Hello, {input_name}')
player_rating = get_rating(input_name)

game_options = input().strip()

if game_options == '':
    game_options = list(combinations.keys())
else:
    game_options = game_options.split(',')

print("Okay, let's start")

while True:
    input_pick = input().strip()

    if input_pick not in (game_options + [COMMAND_EXIT, COMMAND_RATING]):
        print('Invalid input')
        continue

    if input_pick == COMMAND_EXIT:
        break

    if input_pick == COMMAND_RATING:
        print('Your rating: {}'.format(player_rating))
        continue

    input_option = random.choice(game_options)
    result = is_winner(input_pick, input_option, game_options)

    if result is True:
        print(f'Well done. The computer chose {input_option} and failed')
        player_rating += SCORE_WIN
    elif result is False:
        print(f'Sorry, but the computer chose {input_option}')
    else:
        print(f'There is a draw ({input_option})')
        player_rating += SCORE_DRAW

print('Bye!')
