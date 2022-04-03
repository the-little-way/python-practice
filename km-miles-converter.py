# km to miles 1.609 converter

def getKm(x):
    print( f'{x}mi is equal to {x * 1.609} km' )
    
def getMiles(x):
    print( f'{x}km is equal to {x/1.609} miles' )
    
def convertDistance(x):
    # first determine which unit the user typed by slicing the 2nd last letter e.g. 123[k]m or 5[0]m or 123[m]i or 12mil[e]s 
    unitLetters = x[len(x)-2 : len(x)]
    #print(unitLetters)
    # if last 2 characters are km or Km, it means the user wants answer in miles
    # extract numbers, strip whitespace, cast as integer before converting
    remainder = ( x[0 : len(x)-2] ).strip()
    
    if unitLetters == "km" or unitLetters == "Km" or unitLetters == "KM":
        x = int(remainder)
        getMiles(x)
    elif unitLetters == "mi" or unitLetters == "Mi" or unitLetters == "MI":
        x = int(remainder)
        #means user typed in miles so convert to km
        getKm(x)
    else:
         print("Something went wrong. Please type a number, followed by \"km\" or \"mi\" as the distance you want to convert")
         

userIn = input("Type in distance in km or in miles to convert")
convertDistance(userIn)