# search and replace
# a script that identifies and counts how many times a particular word occurs in a string
# allows user to replace all the found words with a new word

# find 'x' everytime it appears in 'y'
def findWord(x, y):
    i = 0
    y = y.split()
    for e in y:
        if e == x:
            i=i+1
    print(i)
    
# replace 'x' everytime it appears in 'y' with 'z'   
def replaceWord(x, y, z):
    #i = 0
    y = y.split()
    for e in range(len(y)):
        if y[e] == x:
            y[e] = z
    y = " ".join(y)
    print("Changes implemented below:\n" + y)
    
# example below replaces 'do', with 'dog'
# replaceWord('do', 'this is the do', 'dog')

strMain = input("Type in a sentence or paragraph you would like to edit:")
strChoice = input("What would you like to do next, type \n (1) to count a specific word, \n (2) to replace a word")

if strChoice == "1":
    strCount = input("Which word would you like to count?")
    findWord(strCount)
    
elif strChoice == "2":
    strRemove = input("Which word would you like to edit?")
    strReplace = input("Which word should it change to?")
    replaceWord(strRemove, strMain, strReplace)
            