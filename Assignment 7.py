# ------------------------------------------------- #
# Title: PickleRick
# Description: A simple example of storing data in a binary file.
# This script tries to make pickling fun
# ChangeLog: (Who, When, What)
# Ehren Williamson,02/25/2021,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
lstData = []
rickFile = "rick.txt"
pickleRickfile = "pickleRick.dat"
lstRick = []


class Processing: # Creates a class to make coding easier

    def convert_file(file_name): # takes a .txt and converts to .dat, makes it easier for mac
        file = open(file_name, "r")
        for item in file:
            lstData.append(item)
        file.close()
        return lstData

    def read_list(list_of_data): # reads a list so I don't have to write it all the time
        for item in list_of_data:
            print(item)

    def save_data_to_file(file_name, list_of_data): ### saves a file as a .dat and pickles it
        file = open(file_name, "wb")
        pickle.dump(list_of_data, file)
        file.close()
        return "Success"

    def read_data_from_file(file_name): ### unpickles a .dat file
        file = open(file_name, "rb")
        list_of_data = pickle.load(file)
        for item in list_of_data:
            print(item)


print("Hello I'm Rick!")
print("I'm here to Pickle a file")
print("********************")
startRick = Processing.convert_file(rickFile)
Processing.save_data_to_file(pickleRickfile, startRick)
print("I don't feel so good.")
print("I'm Pickle rick!")
Processing.read_data_from_file(pickleRickfile)

while (True):
    print("Pickle Rick can now do things!")
    choice = input("""What would you like to do? ## Creates menu
1. Reload Rick
2. Give Rick something to say 
3. Check what Rick is saying
4. Exit
please choose now: """)

    if choice == "1": ### Reads the .dat file
        startRick = Processing.convert_file(rickFile)
        print("Rick is being reset")
        Processing.read_data_from_file(pickleRickfile)
        print()
        print("Rick is reset")
        continue
    elif choice == "2": ### creates a new.dat file from a list of strings created by user
        lstRick.clear()
        newPhrase = input("What is rick's new catchphrase?")
        lstRick.append(newPhrase)
        choices = input("Would you like to add another phrase[Y/N]")
        while (choices.lower() != "n"):
            continuePhrase = input("What other phrase would you like to add?")
            lstRick.append(continuePhrase)
            choices = input("Would you like to add another phrase[Y/N]")
            if choices.lower() == "n":
                continue
        Processing.save_data_to_file(pickleRickfile, lstRick)
        print("Here is the current catchphrase or catchphrases.")
        Processing.read_data_from_file(pickleRickfile)
    elif choice == "3": # Just reads the .dat file
        Processing.read_data_from_file(pickleRickfile)
        continue

    elif choice == "4": # exits program
        print()
        print("Goodbye! \nWubba lubba dub dub")
        break
    else:
        print("Rick is confused, try again" + "\n")
        continue


