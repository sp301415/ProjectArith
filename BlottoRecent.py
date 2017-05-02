import random
import math
profileA = []
profileB = []
valueA = []
valueB = []
scoreA = 0
scoreB = 0
poolA = []
poolB = []
n = int(input("Total Troops: ") )
k = int(input("Total Battlefields: "))
v = int(input("Total Value: "))


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

def calculateScore(valueA, valueB, profileA, profileB, scoreA, scoreB, k):
        for i in range(0, k):
                 if(profileA[i] > profileB[i]) :
                     scoreA = scoreA + valueA[i]
                 if(profileA[i] == profileB[i]):
                     scoreA = scoreA + (valueA[i] * 0.5)
                     scoreB = scoreB + (valueB[i] * 0.5)
                 if(profileA[i] < profileB[i]):
                     scoreB = scoreB + valueB[i]
        
        return (scoreA, scoreB)
    # calculate score once

def reduceOversupply(profileA, profileB):
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

def distributeA(profileA, leftoverA):
    while leftoverA > 0:
            j = random.randint(0,k-1)
            profileA[j] = profileA[j] + 1
            leftoverA = leftoverA - 1

            return profileA
    # Distribute leftover randomly - A

def distributeB(profileB, leftoverB):
    while leftoverB > 0:
            j = random.randint(0,k-1)
            profileB[j] = profileB[j] + 1
            leftoverB = leftoverB - 1

            return profileB
    # DIStribute leftover randomly - B

def spanPoolA(profileA, leftoverA, poolA):
    i = 0
    buffA = []
    buffA = profileA
    while i < 5 :
        profileA = buffA
        poolA.append(distributeA(profileA,leftoverA))
        
    return poolA
    


troopProfile(n,k)
valueProfile(v,k)
scoreA, scoreB = calculateScore(valueA, valueB, profileA, profileB, scoreA, scoreB, k)
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

profileA, profileB = reduceOversupply(profileA, profileB)
leftoverA, leftoverB = (leftoverA, leftoverB)
print (profileA)
print (profileB)
profileA = distributeA(profileA, leftoverA)
profileB = distributeB(profileB, leftoverB)
print (profileA)
print (profileB)

print (poolA)