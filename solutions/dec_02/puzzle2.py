def match_result(opponent_play, your_play):
    if opponent_play == 'A' and your_play == 'X' or opponent_play == 'B' and your_play == 'Y' or opponent_play == 'C' and your_play == 'Z':
        return "draw"
    elif opponent_play == 'A' and your_play == 'Y' or opponent_play == 'B' and your_play == 'Z' or opponent_play == 'C' and your_play == 'X':
        return "win"
    else:
        return "lose"

def number_of_points(your_play, match_result):
    score = 0
    if match_result == "draw":
        score += 3
    if match_result == "win":
        score += 6
    if your_play == "X":
        score += 1
    if your_play == "Y":
        score += 2
    if your_play == "Z":
        score += 3
    return score

if __name__ == "__main__": 
    input = open("puzzle_2_input.tsv").readlines()
    total_score = 0
    for play in input:
        result = match_result(play[0], play[2])
        total_score += number_of_points(play[2], result)
    print("total points you made are:", total_score)

    
