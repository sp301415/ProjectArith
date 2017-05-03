import random
import math


TROOP_TOTAL = int(input("Total Troops: "))
BATTLEFIELD_TOTAL = int(input("Total Battlefied: "))
VALUE_TOTAL = int(input("Total Value: "))


def partition(number, part):
    answer = [0]*part
    for i in range(0, number):
        answer[random.randrange(0, part)] += 1
    return answer


def game(troop_profile, value_profile):  # calculates score
    score = [0, 0]
    for i in range(BATTLEFIELD_TOTAL):
        if troop_profile[0][i] > troop_profile[1][i]:
            score[0] += value_profile[0][i]
        elif troop_profile[0][i] == troop_profile[1][i]:  # each gets half of value if tied
            score[0] += value_profile[0][i] * 0.5
            score[1] += value_profile[1][i] * 0.5
        else:
            score[1] += value_profile[1][i]
    return score


def reduce_improve(troop_profile, player):
    leftover = 0
    opponent = player ^ 1

    # reduce oversupply
    for i in range(BATTLEFIELD_TOTAL):
        if troop_profile[player][i] > troop_profile[opponent][i] + 1:
            leftover += troop_profile[player][i] - troop_profile[opponent][i] - 1
            troop_profile[player][i] = troop_profile[opponent][i] + 1
    print(leftover)

    # improve profile
    while leftover > 0:
        troop_profile[player][random.randrange(0, BATTLEFIELD_TOTAL)] += 1
        leftover -= 1

    return troop_profile


def main():
    troop_profile = [[0 for col in range(BATTLEFIELD_TOTAL)] for row in range(2)]
    troop_profile[0] = partition(TROOP_TOTAL, BATTLEFIELD_TOTAL)
    troop_profile[1] = partition(TROOP_TOTAL, BATTLEFIELD_TOTAL)
    value_profile = [[0 for col in range(BATTLEFIELD_TOTAL)] for row in range(2)]
    value_profile[0] = partition(VALUE_TOTAL, BATTLEFIELD_TOTAL)
    value_profile[1] = partition(VALUE_TOTAL, BATTLEFIELD_TOTAL)
    # gene_pool = [[0 for col in range(BATTLEFIELD_TOTAL)] for row in range(10)]

    print(troop_profile)
    print(value_profile)
    print(game(troop_profile, value_profile))

main()