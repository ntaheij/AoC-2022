CHOICES = ("scissors", "paper", "rock")

opponent = {
    "A": CHOICES[2],
    "B": CHOICES[1],
    "C": CHOICES[0]
}

player = {
    "X": CHOICES[2],
    "Y": CHOICES[1],
    "Z": CHOICES[0]
}

def get_score(opponent_choice, player_choice):
    opp_choice_value = CHOICES.index(opponent[opponent_choice])
    ply_choice_value = CHOICES.index(player[player_choice])
    
    res = len(CHOICES) - CHOICES.index(player[player_choice])

    # Switch difference between indexes:
    #   -1: reading from left to right. If the difference is 1, the player wins 
    # (ex: "scissors" for player, "paper" for opponent) --> +6 points
    #   0: player and opponent did the same choice (= draw) --> +3 points
    #   2: player choose "rock" and opponent "scissors". The player wins --> +6 points
    # NOT IN THE LIST:
    #   1: reading from right to left. If the difference is 1, the player loses
    # (ex: "paper" for player, "scissors" for opponent)
    switch = {
        -1: 6,
        0: 3,
        2: 6,
    }

    return res + switch.get((ply_choice_value - opp_choice_value), 0)

# Method 1:
#   Opponent has three choices: "A" for Rock, "B" for Paper, "C" for Scissors
#   Player has three choices  : "X" for Rock, "Y" for Paper, "Z" for Scissors
#   The input gives the game and we have to calculate the score of the player
# Method 2:
#   Opponent has the same choices
#   Player has three choices: "X" to lose, "Y" to draw (tied game), "Z" to win
#   The input gives the game of the opponent, the strategy for the player
#     and we have to choose the best solution to respect the strategy defined
#     by "X", "Y" or "Z"
def main(method=1):
    score = 0
    with open("inputs/input.txt", "r") as f:
        rounds = [line.rstrip("\n").split() for line in f.readlines()]
        for round in rounds:
            if method == 1:
                score += get_score(round[0], round[1])
            else:
                player_scores_from_key = list(map(lambda key: get_score(round[0], key), list(player.keys())))

                if round[1] == "X": # want to lose
                    score += min(player_scores_from_key)
                elif round[1] == "Z": # want to win
                    score += max(player_scores_from_key)
                else: # want to draw
                    # we must do the same choice as the opponent
                    opponent_choice_to_player = list(filter(lambda item: item[1] == opponent[round[0]], list(player.items())))[0][0]
                    score += get_score(round[0], opponent_choice_to_player)

        return score

print(f'First part: {main()}')
print(f'Second part: {main(method=2)}')