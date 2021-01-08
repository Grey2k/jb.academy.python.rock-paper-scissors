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


def is_winner(pick: str, option: str):
    if combinations[pick] == option:
        return False
    if combinations[option] == pick:
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

while True:
    input_pick = input().strip()

    if input_pick not in (list(combinations.keys()) + [COMMAND_EXIT, COMMAND_RATING]):
        print('Invalid input')
        continue

    if input_pick == COMMAND_EXIT:
        break

    if input_pick == COMMAND_RATING:
        print('Your rating: {}'.format(player_rating))
        continue

    input_option = random.choice(list(combinations.keys()))
    result = is_winner(input_pick, input_option)

    if result is True:
        print(f'Well done. The computer chose {input_option} and failed')
        player_rating += SCORE_WIN
    elif result is False:
        print(f'Sorry, but the computer chose {input_option}')
    else:
        print(f'There is a draw ({input_option})')
        player_rating += SCORE_DRAW

print('Bye!')
