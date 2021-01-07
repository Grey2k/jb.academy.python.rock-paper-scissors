import random

# Write your code here
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

COMMAND_EXIT = '!exit'

combinations = {ROCK: PAPER, PAPER: SCISSORS, SCISSORS: ROCK}


def is_winner(pick: str, option: str):
    if combinations[pick] == option:
        return False
    if combinations[option] == pick:
        return True

    return None


# Entrypoint
while True:
    input_pick = input().strip()

    if input_pick not in (list(combinations.keys()) + [COMMAND_EXIT]):
        print('Invalid input')
        continue

    if input_pick == COMMAND_EXIT:
        break

    input_option = random.choice(list(combinations.keys()))
    result = is_winner(input_pick, input_option)

    if result is True:
        print(f'Well done. The computer chose {input_option} and failed')
    elif result is False:
        print(f'Sorry, but the computer chose {input_option}')
    else:
        print(f'There is a draw ({input_option})')

print('Bye!')
