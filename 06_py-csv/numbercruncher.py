'''
Spreadsheet Saiyans: Shinji Verit
SoftDev
K06 duo mission
2022-09-30
Time spent: 0.8 hours
DISCO:
QCC:
'''

import random as rng

file = open("occupations.csv", "r")
unparsed = file.read()

def csv_to_dict(data):
    result = {}
    lines = data.split("\n")
    lines = lines[1:len(lines)-1]
    for oneline in lines:
        if '"' in oneline:
            oneline = oneline[1::]
            values = oneline.split('"')
#           print(oneline) -> shows that oneline stays unchanged when using oneline.split()
            values[1] = values[1][1::]
            result[values[0]] = float(values[1])
        else:
            values = oneline.split(",")
            result[values[0]] = float(values[1])
    return result

'''
My idea: Take a random number in the range of 0-99.8 (0 to the total percentage given) and set a variable currentval = 0. Then,
loop through all of the key-pairs in the dictionary and check if the random number is in the range of (currentval, currentval +
the percentage of that specific occupation). If it is, print the occupation corresponding to that key pair. Else, currentval =
currentval + the percentage of that specific occupation and then keep looping through the key-pairs.
EX: Random value a, is chosen as 47.2,
-Key-pair 1 = ('Management': 6.1). 47.2 is not between (0,6.1), currentval = 6.2.
-Key-pair 2 = ('Business and Financial operations': 5.0). 47.2 is not betweeen (6.2,11.2), currentval = 11.2
-Keep going until we get key-pair where 47.2 is between (currentval, currentval + percentage) and then return the occupation
associated with that key-pair.
Use dict.items() to get a list of the key-value pairs
'''
def weighted_random(dnary):
    randval = rng.uniform(0,dnary["Total"]) ## Between 0 and the total percentage
    for i in dnary.items():
        print(i)
    return


a = csv_to_dict(unparsed)
print(a)
print("\n")
weighted_random(a)
