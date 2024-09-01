import os
import random
import sys
import string
import time
from libs import keyauth

# Get a logo from https://patorjk.com/software/taag/
logo = """
  .-.                                   
 /    \                                 
 | .`. ;   ___ .-.      .--.     .--.   
 | |(___) (   )   \    /    \   /    \  
 | |_      | ' .-. ;  |  .-. ; |  .-. ; 
(   __)    |  / (___) |  | | | |  | | | 
 | |       | |        |  |/  | |  |/  | 
 | |       | |        |  ' _.' |  ' _.' 
 | |       | |        |  .'.-. |  .'.-. 
 | |       | |        '  `-' / '  `-' / 
(___)     (___)        `.__.'   `.__.'  
                                        
                                        
"""

def genSerials():
    # Generate random serials
    serial = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16))
    return serial


# Keyauth prerequisites
APP_NAME = "app name"
OWNER_ID = "owner id"
APP_SECRET = "secret"
APP_VERSION = "1.0"  
HASH = "browns?"

keyauthapp = keyauth.api(
    name=APP_NAME,
    ownerid=OWNER_ID,
    secret=APP_SECRET,
    version=APP_VERSION
    hash_to_check=HASH
)

os.system("cls")
print(logo + "\n\n")
key = input("Enter your key: ")

# Keyauth
# Probably doesn't work, lmk if it doesn't 
try:
    keyauthapp.license(key)
    print("Key validated successfully.")
except Exception as e:
    print(f"Authentication failed: {str(e)}")
    print("Exiting!")
    time.sleep(3)
    sys.exit()

# Basic choices
os.system("cls")
print(logo + "\n\n")
choice = input("[1] Spoof\n[2] Exit\n\nEnter your choice: ")

if choice == "1":
    # Spoofing
    os.system("AMIDEWINx64.EXE /IVN \"AMI\"")
    os.system("AMIDEWINx64.EXE /SP \"System product name\"")
    os.system("AMIDEWINx64.EXE /SV \"System product name\"")
    os.system("AMIDEWINx64.EXE /SS \"" + genSerials() + "\"")
    os.system("AMIDEWINx64.EXE /SU AUTO")
    os.system("AMIDEWINx64.EXE /SK \"To Be Filled By O.E.M\"")
    os.system("AMIDEWINx64.EXE /BM \"AsRock\"")
    os.system("AMIDEWINx64.EXE /BP \"*8560M-C\"")
    os.system("AMIDEWINx64.EXE /BS \"" + genSerials() + "\"")
    os.system("AMIDEWINx64.EXE /BT \"Default String\"")
    os.system("AMIDEWINx64.EXE /BLC \"Default String\"")
    os.system("AMIDEWINx64.EXE /CM \"Default String\"")
    os.system("AMIDEWINx64.EXE /CV \"Default String\"")
    os.system("AMIDEWINx64.EXE /CS \"" + genSerials() + "\"")
    os.system("AMIDEWINx64.EXE /CA \"Default String\"")
    os.system("AMIDEWINx64.EXE /CSK \"SKU\"")
    os.system("AMIDEWINx64.EXE /PSN \"To Be Filled By O.E.M\"")
    os.system("AMIDEWINx64.EXE /PAT \"To Be Filled By O.E.M\"")
    print("Spoofing Complete! Exiting...")
    time.sleep(3)
    sys.exit()


# Exit binds
elif choice == "2":
    print("Exiting!")
    time.sleep(3)
    sys.exit()

else:
    print("Invalid choice! Exiting!")
    time.sleep(3)
    sys.exit()
