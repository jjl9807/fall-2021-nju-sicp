from functools import lru_cache
PLAYER_NAME = 'Nolan'
MAX_DICE, SIDES, GOAL_SCORE = 10, 6, 50

@lru_cache(maxsize=10000)
def swine_swap(score, opponent_score):
    excitement = str(pow(3, score + opponent_score))
    if excitement[0] == excitement[-1]:
        return True
    return False

@lru_cache(maxsize=10000)
def picky_piggy(opponent_score):
    if opponent_score == 0:
        return 1
    return (9047619 // pow(10, 6 - opponent_score%6)) % 10

@lru_cache(maxsize=10000)
def final_strategy(score, opponent_score):
    max_prob, best_roll = 0, 0
    for n in range(MAX_DICE + 1):
        prob =  prob_of_winning_rolling_n(score, opponent_score, n)
        if prob > max_prob:
            max_prob, best_roll = prob, n
        if prob == 1:
            break
    return best_roll

@lru_cache(maxsize=10000)
def prob_of_winning_rolling_n(score, opponent_score, n):
    if n == 0:
        if picky_piggy(opponent_score) == 0:
            return 0
        return winning_prob(score + picky_piggy(opponent_score), opponent_score)
    result = 0
    for p in range(1, SIDES*n + 1):
        result += prob_of_scoring_p(p, n) * winning_prob(score + p, opponent_score)
    return result

@lru_cache(maxsize=10000)
def ways_to_score_p(p, number_of_dice):
    if p < 0:
        return 0
    elif p == 0 and number_of_dice == 0:
        return 1
    elif number_of_dice == 0:
        return 0
    count = 0
    for i in range(2, SIDES + 1):
        count += ways_to_score_p(p - i, number_of_dice - 1)
    return count

@lru_cache(maxsize=10000)
def prob_of_scoring_p(p, n):
    if p == 1:
        return 1 - pow((SIDES-1)/SIDES, n)
    return ways_to_score_p(p, n) / pow(SIDES, n)

@lru_cache(maxsize=10000)
def winning_prob(score, opponent_score):
    if swine_swap(score, opponent_score):
        score, opponent_score = opponent_score, score
    if score >= GOAL_SCORE:
        return 1
    elif opponent_score >= GOAL_SCORE:
        return 0
    opponent_roll = final_strategy(opponent_score, score)
    return 1 - prob_of_winning_rolling_n(opponent_score, score, opponent_roll)