#This prints all the vals in the dict
newDict = {'key1':'val1','key2':'val2'}
for key in newDict:
    print(newDict[key])

newList = []
for key in newDict:
    newList.append(newDict[key])

print(newList)
