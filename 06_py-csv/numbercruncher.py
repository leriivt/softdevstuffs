'''
Spreadsheet Saiyans: Shinji Verit
SoftDev
K06 duo mission
2022-09-30
Time spent: 0.8 hours

DISCO:
The original string remains unchanged withn using .split()

QCC:
Is it important to account for the 0.2% not part of the total or is it negligible?
'''

import random as rng

occ_file = open("occupations.csv", "r")

def csv_to_dict(file):
    data = file.read()
    result = {}
    lines = data.split("\n") #creates list of all the lines in the csv file
    lines = lines[1:len(lines)-1]

    for oneline in lines:
        if '"' in oneline: #checks for when there is an occupation containing commas
            oneline = oneline[1::] #removes first quotation mark
            values = oneline.split('"') #splits string on second quotation mark, creating a list with the two halves and removes the quotation mark
#           print(oneline) -> shows that oneline stays unchanged when using oneline.split()
            values[1] = values[1][1::] #removes the unwanted comma currently part of the string percentage: ",6.1" --> "6.1"
            result[values[0]] = float(values[1]) #adds occupation,percentage pair to dictionary while converting string percentage to float
        else:
            values = oneline.split(",") #splits string on comma, creating a list with the two halves and removes the comma
            result[values[0]] = float(values[1]) #adds occupation,percentage pair to dictionary while converting string percentage to float
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
    print(randval)
    current_val = 0
    for i in dnary.keys():
        if randval >= current_val and randval < current_val + dnary[i]:
            return i
        else:
            current_val += dnary[i]


a = csv_to_dict(occ_file)
print(a)
print("\n")
print(weighted_random(a))
