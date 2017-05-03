import random
import math

TROOP_TOTAL = int(input("Total Troop: "))
BATTLEFIELD_TOTAL = int(input("Total Battlefield: "))
VALUE_TOTAL = int(input("Total Value: "))


def game(troop_profile, value_profile):  # calculates score
    score = [0, 0]
    for i in range(0, BATTLEFIELD_TOTAL):
        if troop_profile[0][i] > troop_profile[1][i]:
            score[0] += value_profile[0][i]
        elif troop_profile[0][i] == troop_profile[1][i]:  # each gets half of value if tied
            score[0] += value_profile[0][i] * 0.5
            score[1] += value_profile[1][i] * 0.5
        else:
            score[1] += value_profile[1][i]
    return score


def random_distribute(array):

    # randomly distribute code here

    return array


def reduce_improve(troop_profile, player):
    leftover = 0
    opponent = player ^ 1

    # reduce oversupply
    for i in range(0, BATTLEFIELD_TOTAL):
        if troop_profile[player][i] > troop_profile[opponent][i] + 1:
            leftover += troop_profile[player][i] - troop_profile[opponent][i] - 1
            troop_profile[player][i] = troop_profile[opponent][i] + 1
    print(leftover)

    # improve profile
    while leftover > 0:
        troop_profile[player][random.randint(0, BATTLEFIELD_TOTAL)] += 1
        leftover -= 1

    return troop_profile


def main():
    troop_profile = [[0 for col in range(BATTLEFIELD_TOTAL)] for row in range(2)]
    value_profile = [[0 for col in range(BATTLEFIELD_TOTAL)] for row in range(2)]
    gene_pool = [[0 for col in range(BATTLEFIELD_TOTAL)] for row in range(10)]

    print(game(troop_profile, value_profile))


main()