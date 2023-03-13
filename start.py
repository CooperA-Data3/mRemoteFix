# Importing Modules
import animation
import getpass
import os
import sys
import random
import time
import subprocess
import pyperclip

# Plays a loading animation for startup
@animation.wait("spinner")


# Loads all modules
def imports():
    print("Loading")
    time.sleep(random.randint(1,5))
    print("Done\n")

# Start Main Functions
imports()


# This is executed at the end of the program.
# It tells the user that I'm bad at coding and if it doesn't work to bear with me and do it manually
# It then opens up the folder where the file should be there, so the user can verify my spaghetti code somehow worked

def finish_up():
    print("Please check to see if there is ONLY ONE FILE, named 'hosts' in the folder that is about to launch.\nIf there isn't, open the README.txt file and move files manually.\nSorry if it doesn't work perfectly I'm bad at coding")
    time.sleep(random.randint(5,10))
    driver_dir = "C:/Windows/System32/drivers/etc"
    start_driver_dir = os.path.realpath(driver_dir)
    os.startfile(start_driver_dir)
    exit()



# This is executed before the "del_files" function,
# but because the "del_files" function calls this one, it must be above it.
# Opens a CMD command to move the "hosts" file into the drivers\etc folder

def replace_files():
    PathToScript_Replace = "ReplaceFiles.lnk"
    
    print("\n \nWhen prompted, enter administrator username and password.")
    time.sleep(5)
    os.system('cmd /c "start /MIN ReplaceFiles.lnk"') # Starts the CMD script
    time.sleep(3)
    finish_up() # Starts the final stretch of the code



# Runs the CMD script to delete all existing files in drivers\etc 
def del_files():
    PathToFiles = "C:\\Windows\\System32\\drivers\\etc"
    PathToScript_Delete = "DeleteFiles.lnk"

    print("\n \nWhen prompted, enter administrator username and password.")
    time.sleep(5)
    os.system('cmd /c "start /MIN DeleteFiles.lnk"')
    time.sleep(3)
    replace_files() # After files are deleted, replace them


# This part asks user to confirm they have added their username to the "ReplaceFiles.cmd" script
# If the user confirms they have finished instructions, continue
# If they type anything other than "done", insult the user for lack of spelling skills, then terminate

def confirm_finished():
    confirm = input("Type 'done' when you've added your username to the file:\n>> ")
    if confirm == "done":
        del_files()
        
    else:
        print("Error: User doesn't know how to spell 'done'. Terminating...")
        time.sleep(3)
        exit()
        

# Copies the username of the user so they can paste it into the "ReplaceFiles.cmd" program instead of typing it.
# I know, I know, how thoughtful of me.

def copy_username():
    username = getpass.getuser()
    #print(username) # DEBUG
    pyperclip.copy(username)
    print("Your username has been copied to your clipboard.\n")
    print("When a window pops up after this message, right click on 'ReplaceFiles.cmd' and press 'Edit'\nThen delete 'USERNAME_HERE' and replace it with your username (Using 'ctrl + V')")
    time.sleep(5)
    directory = "C:/Users/%s/Documents/mRemoteFix" % username
    startdirectory = os.path.realpath(directory)
    os.startfile(startdirectory)
    confirm_finished()


# Starts the script
copy_username()



