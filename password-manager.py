# dependencies
# pip install cryptography
import random
from cryptography.fernet import Fernet

"""
# create key file, uncomment section below on first use
def writeKey():
	key = Fernet.generate_key()
	with open('key.key', 'wb') as keyFile:
		keyFile.write(key)

writeKey()
"""


#load key for decryption
def loadKey():
	key = open("key.key", "rb").read()
	#key.close()
	return key

##the random password generator, lim - 8 characters long

def genPass():
	alphaNum = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '#', '$' ]
	i = 0
	lim = 8
	results = []

	while i < lim:
		x = random.randrange(1, int(len(alphaNum)))
		results.append(alphaNum[x])
		if i == lim:
			break
		i = i+1
	#force atleast 1 special char at end
	results[lim-1] = '$'
	final = "".join(results)
	return final


## the features i.e. (1) show passwords, (2) add new password

def showPass():
    authUser = input("Type in your master password to continue:")
    newKey = loadKey() + authUser.encode()
    fer = Fernet(newKey)

    with open('passwords.txt', 'rb') as file:
    	for line in file:
    		results = file.readline()
    		print(fer.decrypt(results))


def addPass():
	while True:

	    authUser = input("Type in your master password to continue:")
	    newKey = loadKey() + authUser.encode()
	    fer = Fernet(newKey)

	    newAccount = input("Type in the account username or email adress you want to save:")

	    print(f"Please confirm there are no typos. You typed: {newAccount}")

	    emailCheck = input("Y/N:").lower()

	    if emailCheck == "y":
	        newPass = genPass()

	        passCheck = input(f"""New password generated: {newPass}
	            Type \"Y\" to keep the generated password
	            Type \"N\" to manually type-in your own:""")

	        if passCheck == "y":
	            saveToFile(newAccount, newPass, authUser, fer)
	            break

	        elif passCheck == "n":
	            newPass = input("Type in your own new password to use instead:")
	            saveToFile(newAccount, newPass, authUser, fer)
	            break
	          
	    else:
	        continue


## save info to file, a - newaccount, b - new password, c - authenticate, d - key

def saveToFile(a, b, c, d):
    if c == "admin":
        fer = d
        with open("passwords.txt", "a") as file:
          info = f"\nUser account: {a}\nPassword: {b}"
          encryptedInfo = fer.encrypt(info.encode())
          file.write((encryptedInfo).decode() + "\n")
          print("New account and password successfully saved!")

    else:
    	print("Oops, something went wrong...")


## welcome to password manager

getMode = input("""Welcome to EasyPy, a simple password manager -
Type \"view\" to view your saved passwords
Type \"add\" to add a new password for storage
:""").lower()


while True:
    if getMode == "q":
        print("You have successfully logged out.")
        break
    
    elif getMode == "view":
        showPass()
        break
	        
    elif getMode == "add":
        addPass()
        break
	        
    else:
        print("Sorry, you typed an invalid option")
        continue
