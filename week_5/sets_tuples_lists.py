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
    
