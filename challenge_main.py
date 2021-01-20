### 20/01/2021
### Toby Rutherford
### File Manager Python Application

import time
import json
import os

# Importing external functions
import challenge_functions as cf

# Load previous default directory
def_dir = []
def_dir_file = 'default_directory.json'
try:
    with open(def_dir_file, 'r+') as file_object:
        directory_load = json.load(file_object)
except FileNotFoundError:
    begin_file = ""
    with open(def_dir_file, 'w') as file_object:
        json.dump(begin_file, file_object)
        print("\nCreating default directory file...")
        new_def = input("\nEnter new default directory: ")
        if os.path.isdir(new_def):
            print("\nExisting directory under that name...")
            print("\nPlease set a default directory from the menu...")
        else:
            def_dir.append(new_def)
            os.mkdir(new_def)
            print("\nSetting new default directory...")
except json.decoder.JSONDecodeError:
    print('\nNo directory to load from file.')
else:
        print("\nLoading default directory file...")
        for directory in directory_load:
            def_dir.append(directory)
str_dir = str(def_dir)
pass_dir = ''.join(c for c in str_dir if c not in "[']")

# Intro to File Manager ---------------- Start of visible code
time = time.asctime()
print("\n########### Python File Manager ###########")
print("\nThe current time and date is: " + time)

# All usable functions within the program
while True:
    # Work with multiline string for input --- WIP
    pro_input = input(
    "\nWhich process would you like to perform?"
    "\n\n1. Read an existing file."
    "\n2. Write a new file or overwrite an existing file."
    "\n3. Append to an existing file."
    "\n4. Delete a file."
    "\n5. Move a file."
    "\n6. Copy a File."
    "\n7. Check if a file exists."
    "\n8. List files in a directory."
    "\n9. Count all files within a directory and subdirectories."
    "\n10. Create a new directory."
    "\n11. Delete an existing directory."
    "\n12. Create a potential default directory."
    "\n13. Set default/root file directory."
    "\n14. Check operating system."
    "\n15. Exit program."
    "\n\nEnter Here: ")

    if pro_input == '1':
        cf.Read(pass_dir)

    elif pro_input == '2':
        cf.Write(pass_dir)

    elif pro_input == '3':
        cf.Append(pass_dir)

    elif pro_input == '4':
        cf.Delete(pass_dir)

    elif pro_input == '5':
        cf.Move(pass_dir)

    elif pro_input == '6':
        cf.Copy(pass_dir)

    elif pro_input == '7':
        cf.Check(pass_dir)

    elif pro_input == '8':
        cf.List(pass_dir)

    elif pro_input == '9':
        cf.Count(pass_dir)

    elif pro_input == '10':
        cf.CreateDir(pass_dir)
    
    elif pro_input == '11':
        cf.DeleteDir(pass_dir)
    
    elif pro_input == '12':
        cf.CreateDefDir()

    # Reassigns json file that store name of default/root file directory so as not to clog main project folder
    elif pro_input == '13':
        # Sets default directory for next load
        new_def = input("\nEnter new default directory: ")
        if os.path.isdir(new_def):
            def_dir[0] = new_def
            print("\nSetting new default directory...")
        else:
            print("Not a valid directory...")
        
        # Loads default directory changes into file for next load - Auto save after default directory change.
        try:
            with open(def_dir_file, 'w') as file_object:
                json.dump(def_dir, file_object)
        except FileNotFoundError:
            print("\nCould not save information from this session!")
        else:
            print("\nAuto-save...")
        
    elif pro_input == '14':
            cf.CheckOS()
    
    elif pro_input == '15':

        # Loads default directory changes into file for next load if user exits
        try:
            with open(def_dir_file, 'w') as file_object:
                json.dump(def_dir, file_object)
        except FileNotFoundError:
            print("\nCould not save information from this session!")
        else:
            print("\nAuto-save...")

        cf.Exit()

    # Ask user whether they want to compelte another process or quit program.
    con_input = input("\nDo you want to continue working? \n\n 'Yes' or 'No' \n\n Enter Here: ")
    if con_input == 'Yes':
        print('\nReturning to menu...') 
    else:
        cf.Exit()