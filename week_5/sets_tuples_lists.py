# collection = single "variable" used to store mutiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut", "watermelon", "strawberry", "mango"]

print(dir(fruits))
# all the attriubtes for the list

print(help(fruits))
# gives you a description of the documentation

print(len(fruits))
# gives length of list

print("pineapple" in fruits)
# sees if the word is in list

print(fruits[::2])  
# removes every second element

print(fruits[::-1])
# prints everything backwards

print(fruits[0])
# prints element 

fruits[1] = "banana"
# changes the index to the set variable

fruits.append("pineapple")
# adds to the end of the list

fruits.remove("apple")
# removes the fruit

fruits.insert(0, "kiwi")
# adds pineapple and pushes everything down

fruits.sort()
# it orders everything in alphabetical order

fruits.reverse()
# reverse alphabetical order

fruits.clear()
# removes all the elements

print(fruits.index("apple"))

# print(fruits)

 for fruit in fruits:
    print(fruit)
#iteration

##########sets###########
# sets are unordered and unindexed
# they are defined using curly brackets
# they do not allow duplicates
# fruits = {"apple", "banana", "mango", "cherry", "watermelon"}
# print(fruits)
# print(dir(fruits)) # attribute that can be used with sets
# print(help(fruits)) # documentation/methods that can be used with sets
# print(len(fruits)) # number of elements in set
# print("volvo" in fruits) # check if an element is in the set

# add an element to the set
# print(fruits.add("orange"))
# print(fruits)
# print(fruits.add("kiwi"))
# print(fruits)
# add mutiple elements to the set
# print(fruits.update(["orange", "kiwk", "pineapple"]))
# print(fruits)

# #remove an element from the set
# print(fruits.remove("banana"))
# print(fruits)
# print(fruits.pop()) # removes the last element in the set
# print(fruits)
# print(fruits.clear()) # clears the set
# print(fruits)

# when do we want to use sets?
# sets are useful when you want to store a collection of items that should not be changes, and you do not care about the order of the items
#example: a collections of unique items
social_security_numbers = {123456789, 987654321, 123456789}
# remove the last element in this set
# add another social security number
print(social_security_numbers.add(843932843))
print(social_security_numbers)

###########tuples###########
# tuples are immutable and are defined using parentheses
# create a tuple called my_tuple with the following values:
example_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(example_tuple)
# print(example_tuple.count(2))
# # the value 2 appears in the tuple
# print(dir(example_tuple)) # attributes that can be used with tuples
# print(help(example_tuple)) # documentation/methods that can be used with tuples
# print(len(example_tuple)) # number of elements in the tuple
# print(2 in example_tuple) # check if an elemeent is in tuple
# # when are they useful?
# # Tuples are useful when you want to store a collection of item that should not be change, such as days of the week, months of the year, etc.
# # if you want to find the index of a value in a tuple
# print(example_tuple.index(2))
# lymeric = "peter pipen picked a peck of pickled peppers peppers"
# # convert string to a tuple
# # split it first
# lymeric_tuple = tuple(lymeric.split())
# print(lymeric_tuple)
# # find how many the times the word "peppers" appears in the tuple
# print(lymeric_tuple.count("peppers"))

#loops with tuples
for item in example_tuple:
    print(item)


############dictionary###############
# dictionaries are unordered, changeable and indexed 
# they are defined using curly brackets
# they have keys and values
# a collection of {key:value} pairs, no duplicates
# key are unique
# values can be of any data type
capitals = {"Keyna":"Nairobi",
            "Uganda":"Kampala",
            "Tanzania":"Dodoma",
            "Rwanda":"Kigali",
            "China":"Beijing",
            "USA":"Washington DC"}
print(capitals)
# print(dir(capitals)) # attributes that can be used with dictionaries
# print(help(capitals)) # documentations/methods that can be used with dicionaries
# print(len(capitals)) # numbers of items in the dictionary
# if you want to check the value of a is in the dictionary
print(capitals["Keyna"])
print(capitals.get("Keyna"))
# add on item to the dictionary
capitals["South Africa"] = "Pretoria"
print(capitals)
capitals.update({"Nigeria":"Abuja"})
# add three more countires and their capitals to the dictionary
capitals.update({"Denmark":"Copenhagen", "Japan":"Tokyo", "Finland":"Helskini"})

capitals.pop("China") # remove an item from dictionary
print(capitals)
# clear the dictionary
# capitals.clear() #do not run this
# loop through the dictionary
for key in capitals:
    print(f"these are the {key}")

for value in capitals.values():
    print(value)

# print the key value pairs in the dictionary
items_all = capitals.items() # key value pairs
for key, value in items_all:
    print(f"{value} is the capital of {key}")
    
