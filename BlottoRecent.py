import random
import math
import statistics
from collections import defaultdict


TROOP_TOTAL = int(input("Total Troops: "))
BATTLEFIELD_TOTAL = int(input("Total Battlefield: "))
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

    # improve profile
    while leftover > 0:
        troop_profile[player][random.randrange(0, BATTLEFIELD_TOTAL)] += 1
        leftover -= 1

    return troop_profile


def generous_mode(troop_profile, value_profile, player):
    opponent_indifferent = []
    score = 0

    indifferent = defaultdict(list)
    for i, item in enumerate(value_profile[player]):
        indifferent[item].append(i)
    indifferent = {k: v for k, v in indifferent.items() if len(v) > 1}  # thanks to stackoverflow

    for x in range(len(indifferent.keys())):
        for y in list(indifferent.values())[x]:
            opponent_indifferent.append(troop_profile[player][y])
        score += statistics.stdev(opponent_indifferent)
        opponent_indifferent.clear()  # Generous Mode Algorithm - to be determined

    return score


def greedy_mode(troop_profile, value_profile, gene_pool, player):
    gene_score = []
    troop_gene = [[], []]
    opponent = player ^ 1
    troop_gene[1] = troop_profile[opponent]
    weight_greedy = 100  # greedy weight- to be determined by several tests
    
    for i in range(len(gene_pool)):
        troop_gene[0] = gene_pool[i]
        gene_score[i] += (game(troop_gene, value_profile)[player] -
                          game(troop_profile, value_profile)[player]) * weight_greedy
        # add difference of score and multiply weight

    return gene_score


def main():
    troop_profile = [[0 for col in range(BATTLEFIELD_TOTAL)] for row in range(2)]
    troop_profile[0] = partition(TROOP_TOTAL, BATTLEFIELD_TOTAL)
    troop_profile[1] = partition(TROOP_TOTAL, BATTLEFIELD_TOTAL)

    value_profile = [[0 for col in range(BATTLEFIELD_TOTAL)] for row in range(2)]
    value_profile[0] = partition(VALUE_TOTAL-BATTLEFIELD_TOTAL, BATTLEFIELD_TOTAL)
    value_profile[1] = partition(VALUE_TOTAL-BATTLEFIELD_TOTAL, BATTLEFIELD_TOTAL)
    for i in range(BATTLEFIELD_TOTAL):
        value_profile[0][i] += 1
        value_profile[1][i] += 1

    gene_pool = [[0 for col in range(BATTLEFIELD_TOTAL)] for row in range(10)]


if __name__ == "__main__":
    main()

