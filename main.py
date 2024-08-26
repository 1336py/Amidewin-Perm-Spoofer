import os
import random
import sys
import string
import time

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
    # Generate serials
    serial = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16))
    return serial

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

elif choice == "2":
    print("Exiting!")
    time.sleep(3)
    sys.exit()

else:
    print("Invalid choice! Exiting!")
    time.sleep(3)
    sys.exit()