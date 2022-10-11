'''
VSM: Verit, Sebastian, Maya
SoftDev
K08 -- introduction to Flask
2022-10-09
time spent: 0.6
'''

from flask import Flask
app = Flask(__name__) #create instance of class Flask

import random as rng

def csv_to_dict(file_name):
    file = open(file_name, "r")
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



def weighted_random(dnary):
    randval = rng.uniform(0, 100)
#     print(randval)
    current_val = 0
    if randval >= dnary["Total"]: #to account of the 0.2% not in total
        return "Other"
    for i in dnary:
        if randval < current_val + dnary[i]:
            return i
        else:
            current_val += dnary[i]


occ_dict = csv_to_dict("occupations.csv")
#print(occ_dict)

heading = \
"VSM: Verit, Sebastian, Maya<br>\n\
SoftDev<br>\n\
K08 -- introduction to Flask<br>\n\
2022-10-09<br>\n\
time spent: 0.6<br><br>\n\n"

#returns a formatted string listing all the occupations
def str_occupations():
    str = '<br><br>List of occupations:'
    for job in list(occ_dict.keys())[:-1]:      # ignore 'total'
        str += '<br>' + job
    return str



@app.route("/")       #assign fxn to route
def hello_world():
    rand_occ = weighted_random(occ_dict)
    print("\n------------------------------------------")
    print("the random occupation is...")
    print(rand_occ)
    print()
    final = heading + '<br>' + rand_occ
    print(final)
    return final + str_occupations()


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
