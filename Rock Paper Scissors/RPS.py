import re

def player(prev_play, opponent_history=[]):
    response = {'R': 'P', 'P': 'S', 'S': 'R'}

    if prev_play:
        guess = response[prev_play]

        opponent_history.append(prev_play)
    else:
        guess = 'R'

    if len(opponent_history) > 100:
        search_pattern = ''.join(opponent_history[-10:])
        history = ''.join(opponent_history[:-2])

        match = re.search(search_pattern, history)

        if match:
            match_index = match.span()[1]
            next_move = opponent_history[match_index]
            guess = response[next_move]

    return guess
