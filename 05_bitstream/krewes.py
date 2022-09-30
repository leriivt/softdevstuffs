import random as rng

'''
Shinji Verit
SoftDev
K05 duo mission
2022-09-28
Time spent: 0.4 hours
DISCO:
Parse parts of strings into a list using split(separator) method
When adding a list to a list, you can put the list you're adding in [] to add the list that has all of the values
as a single element rather than having an element for all of the values in the list seperately.
QCC:
If you just pick a random period/key from a dictionary to pick a random devo, it likely won't actually be truly random
as certain values could be more likely. For example, if there are 3 periods, one has 1 value and the others have 4 values,
the chance of picking the value in the period with one value is 33%, while the chance of picking a specific value in another
period is 1/4 as much. What's the best way to pick a fully random value from the dictionary without putting all of the
values into a list and taking a random one?
'''

file = open("krewes.txt", "r")
unparsed = file.read()

def generate_info(times): ## times is the amount of data/people included in the info
    result = ""
    for i in range(times):
        result += str(rng.randint(1,10)) + "$$$"
        for j in range(2):
            for k in range(3):
                result += chr(65 + rng.randint(0,25))
            if (j == 0):
                result += "$$$"
            elif (i < times - 1):
                result += "@@@"
    return result

def sort_data(data):
    result = {}
    units = data.split("@@@")
    for i in range(len(units)):
        features = units[i].split("$$$")
        if (features[0] in result.keys()):
            result.update({features[0]: result.get(features[0]) + [[features[1], features[2]]]})
        else:
            result[features[0]] = [[features[1], features[2]]]
    return result
        
test1 = sort_data(generate_info(20))

def rand_devo(dnary):
    try:
        all_devos = []
        for i in (dnary.keys()):
            thisperiod = dnary[i]  #gets list at period in dnary
            for j in (thisperiod): #goes through all sublists 
                j.append(i)        #and appends the period number
                all_devos += [j]   #then add to all_devos
        print(all_devos)
        randompick = rng.choice(all_devos)
        print("Name: " + randompick[0] + " Period: " + randompick[2] + " Ducky name: " + randompick[1])
    except:
        print("Error, dict is length 0")
  
'''
print(test1)
print("\n")
rand_devo(test1)
'''

print(unparsed)

print("\n")
parsed = sort_data(unparsed)
print(parsed)
print("\n")
rand_devo(parsed)

#print(generate_info(20))
