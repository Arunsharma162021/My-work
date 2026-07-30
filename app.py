import os
import time
from menu import value
n=value()
if n==1:
    print("opening notes...")
    time.sleep(2)
    os.system("cls")
elif n==2 :
    print("opening tasks...")
    time.sleep(2)
    os.system("cls")
elif n==3:
    print("exiting toolkit...")
    time.sleep(2)
    os.system("cls")
else:
    print("Please give a valid response")
    time.sleep(2)
    os.system("cls")