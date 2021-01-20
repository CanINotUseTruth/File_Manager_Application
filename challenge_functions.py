### 20/01/2021
### Toby Rutherford
### Methods for File Manager Python Application

import json
import os
import platform
import shutil
import time

# Read Function - for existing files will return error if file does not exist
def Read(pass_dir):
    path = pass_dir + "/" + input("\nEnter the file path to read: ")
    file = open(path)
    print(file.read())
    input("\nPress Enter, to continue...")
    file.close()

# Write Function - writes/overwrites a new file
def Write(pass_dir):    
    path = pass_dir + "/" + input("\nEnter the path of file to write or create: ")
    if os.path.isfile(path):
        print('\nRebuilding the existing file...') 
    else:
        print('\nCreating the new file...') 
    text=input("\nEnter text: ")
    file=open(path,"w")
    file.write(text)

# Append Function - Will append text to an existing file or if file does not exist will create from scratch
def Append(pass_dir):    
    path = pass_dir + "/" + input("\nEnter the path of file to append to: ")
    if os.path.isfile(path):
        print('\nLoading the existing file...') 
    else:
        print("\nNo file of that name...")
        con_input = input("\nDo you want to start a new file? \n\n 'Yes' or 'No' \n\n Enter Here: ")
        if con_input == 'Yes':
            print('\nCreating the new file...') 
        else:
            print("Returning to menu...")
            return
    text=input("\nEnter text: ")
    file=open(path,"a")
    file.write("\n")
    file.write(text)

# Delete Function - Will delete given file path
def Delete(pass_dir):
    path = pass_dir + "/" + input("\nEnter the path of file to delete: ")
    if os.path.isfile(path):
        print('\nDeleting the file...')
        os.remove(path) 
    else:
        print("\nNo file of that name...")
        print("\nReturning to menu ...")
        return

# Move Function - Will move given file path to given destination folder
def Move(pass_dir):
    source_path = pass_dir + "/" + input("\nEnter the path of file to move: ")
    destination_path = pass_dir + "/" + input("\nEnter the destination of file: ")
    if os.path.isfile(source_path):
        print('\nMoving the file...')
        shutil.move(source_path, destination_path)

    else:
        print("\nNo file of that name...")
        print("\nReturning to menu ...")
        return

# Copy Function - Will copy given file path to given destination folder
def Copy(pass_dir):
    source_path = pass_dir + "/" + input("\nEnter the path of file to copy: ")
    destination_path = pass_dir + "/" + input("\nEnter the destination of file: ")
    if os.path.isfile(source_path):
        print('\nCopying the file...')
        shutil.copy2(source_path, destination_path)

    else:
        print("\nNo file of that name...")
        print("\nReturning to menu ...")
        return

# Check Function - Will check if a given file path exists
def Check(pass_dir):
    path = pass_dir + "/" + input("\nEnter the path of file to check: ")
    if os.path.isfile(path):
        print('\nGiven file exists.')

    else:
        print("\nNo file of that name...")
        print("\nReturning to menu ...")
        return

# List Function - Will lists all files/subdirectories within a given directory
def List(pass_dir):
    directory = pass_dir + "/" + input("\nEnter which directory will be listed: ")
    if os.path.isdir(directory):
        output = os.listdir(directory)
        item_number = 1
        print("\nItems in directory:")
        for item in output:
            print(str(item_number) + ". " + item)
            item_number += 1
    
    else:
        print("\nNo directory of that name...")
        print("\nReturning to menu ...")
        return

# Count Function - Will count all files within a directory and it's subdirectories
def Count(pass_dir, counter=0):
    directory = pass_dir + "/" + input("\nEnter which directory will be counted: ")
    if os.path.isdir(directory):
        for pack in os.walk(directory):
            for f in pack[2]:
                f # To remove unused variable
                counter += 1
        print("File Count: " + str(counter) + " files")
    
    else:
        print("\nNo directory of that name...")
        print("\nReturning to menu ...")
        return

# Create Directory Function - Will create a new directory within your default/root folder/directory or as otherwise specific ie. sub-subdirectories
def CreateDir(pass_dir):
    new_dir = pass_dir + "/" + input("\nEnter name of new directory: ")
    if os.path.isdir(new_dir):
        print("\nDirectory already exists...")
        print("\nReturning to menu...")
        return

    else:
        print("\nCreating directory...")
        os.mkdir(new_dir)

# Delete Directory Function - Will delete directories/subdirectories as specified and will confirm deletion if there is contents
def DeleteDir(pass_dir):
    del_dir = pass_dir + "/" + input("\nEnter name of directory: ")
    try:
        if os.path.isdir(del_dir):
            os.rmdir(del_dir)
            print("Deleting directory...")

        else:
            print("\nUnknown directory, unable to delete...")
            print("\nReturning to menu...")
    
    except OSError:
        really = input("\nThere are files in that directory! \nAre you sure you want to delete it? \n\n 'Yes' or 'No' \n\n Enter Here: ")
        if really == 'Yes':
            print("\nDeleting directory and contents...")
            shutil.rmtree(del_dir)

        else:
            print("\nReturning to menu...")

# Create Default Directory Function - Will create new root/default directories within the main folder to potentially switch to for organisation
def CreateDefDir():
    new_dir = input("\nEnter name of new directory: ")
    if os.path.isdir(new_dir):
        print("\nDirectory already exists...")
        print("\nReturning to menu...")
        return

    else:
        print("\nCreating directory...")
        os.mkdir(new_dir)

# Check OS Fucntion - Checks system information
def CheckOS():
    print("\nOperating system:")
    osystem = platform.platform()
    print(osystem)

# Exit Function - Will do as it says...
def Exit():
    print("\nActions complete.")
    print("\nClosing the program...")   
    exit()
