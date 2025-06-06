def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    if len(opponent_history) < 5:
        return "R"

    from collections import Counter
    count = Counter(opponent_history)

    most_common = count.most_common(1)[0][0]

    counter_moves = {"R": "P", "P": "S", "S": "R"}

    return counter_moves[most_common]
