import random
import math

TROOP_TOTAL = int(input("Total Troops: "))
BATTLEFIELD_TOTAL = int(input("Total Battlefields: "))
VALUE_TOTAL = int(input("Total Value: "))

'''
def troopProfile (n,k):
        i=0
        while i < int(k) :
            while(i< k-1):
                profileA.append(random.randint(round(n//k)-2, round(n/k)+2))
                profileB.append(random.randint(round(n//k)-2, round(n/k)+2))
                i = i+1
            if(i == k-1):
                profileA.append(n-sum(profileA))
                profileB.append(n-sum(profileB))
                i = i+1
            return profileA
            return profileB
    # troop profile build

def valueProfile (v,k):
        i=0
        while i < int(k) :
            while(i< k-1):
                valueA.append(random.randint(round(v//k)-2, round(v//k)+2))
                valueB.append(random.randint(round(v//k)-2, round(v//k)+2))
                i = i+1
            if(i == k-1):
                valueA.append(v-sum(valueA))
                valueB.append(v-sum(valueB))
                i = i+1
            return valueA
            return valueB
    # value Profile Build
    '''


def game(troop_profile, value_profile, score):  # calculates score
    for i in range(0, len(troop_profile[0])):
        if troop_profile[0][i] > troop_profile[1][i]:
            score[0] += value_profile[0][i]
        elif troop_profile[0][i] == troop_profile[1][i]:
            score[0] += value_profile[0][i] * 0.5
            score[1] += value_profile[1][i] * 0.5
        else:
            score[1] += value_profile[1][i]
    return score


def reduce_oversupply(profileA, profileB):
    global leftoverA
    global leftoverB
    leftoverA = 0
    leftoverB = 0
    for i in range(0, k-1) :
        if(profileA[i] > profileB[i] + 1):
            leftoverA = leftoverA + profileA[i] - profileB[i] - 1
            profileA[i] = profileB[i] + 1
        if(profileB[i] > profileA[i] + 1):
            leftoverB = leftoverB + profileB[i] - profileA[i] - 1
            profileB[i] = profileA[i] + 1
    print (leftoverA, leftoverB)
    return (profileA, profileB)
    # Reduce Oversupply Task

def distribute_A(profileA, leftoverA):
    while leftoverA > 0:
            j = random.randint(0,k-1)
            profileA[j] = profileA[j] + 1
            leftoverA = leftoverA - 1

            return profileA
    # Distribute leftover randomly - A

def distribute_B(profileB, leftoverB):
    while leftoverB > 0:
            j = random.randint(0,k-1)
            profileB[j] = profileB[j] + 1
            leftoverB = leftoverB - 1

            return profileB
    # DIStribute leftover randomly - B

def span_pool_A(profileA, leftoverA, poolA):
    i = 0
    buffA = []
    buffA = profileA
    while i < 5 :
        profileA = buffA
        poolA.append(distributeA(profileA,leftoverA))
        
    return poolA


def main():
    troop_profile = [[0 for col in range(BATTLEFIELD_TOTAL)] for row in range(2)]
    value_profile = [[0 for col in range(BATTLEFIELD_TOTAL)] for row in range(2)]
    gene_pool = [[0 for col in range(BATTLEFIELD_TOTAL)] for row in range(10)]
    score = []

    print(troop_profile)


main()



    
'''

scoreA, scoreB = calculate_score(valueA, valueB, profileA, profileB, scoreA, scoreB, k)
print ("Initial Troop Profile of A is")
print (profileA)
print ("Initial Troop Profile of B is")
print (profileB)
print ("Value Profile of A is")
print (valueA)
print ("Value Profile of B is")
print (valueB)

print ("each Score")
print (scoreA)
print (scoreB)

profileA, profileB = reduce_oversupply(profileA, profileB)
leftoverA, leftoverB = (leftoverA, leftoverB)
print (profileA)
print (profileB)
profileA = distribute_A(profileA, leftoverA)
profileB = distribute_B(profileB, leftoverB)
print (profileA)
print (profileB)

print (poolA)
'''