# creating dictionaries,
<dictionary name = {key1: values, key2: value2}
myDict = {name: "Akinola", Age: 30, Gender: 'M'}
    myDict[name] =
#Creating a large dictionary
myDictionary = { }
    myDictionary[name] = Fola
    myDictionary{Gender} = Female
compSc = { }
compSc["OS"] = ["Operating System"]
compSc["HW"] = ["Hardware"]
compSc["SW"] = ["Software"]
compSc["SaaS"] = ["Software as a Service"]
    word = input ("enter an abbreviation in computiong")
    if word in compSc:
        print("Word found", compSc[word])
    else:
        print(word, "not found in the dictionary")

#python sets
#A set is an unordered collection of items. In a set, every elemennt is unique, no duplicates, its elements are immutable, the set itself is mutable.
#Declaring a set
mySet = {1, 2, [4, 5], (7, 8, 10)}
mySet = { }
#To add elements
mySet.update (2)
mySet.add ((2,4,6))
mySet.add ([1,2,4])
n = input (int("what more to add"))
mySet.add (n)
print(mySet)
setA = {1,2,4,6}
setB = {3,7,5,11}
setC = setA|setB #set union
setD = setA & setB