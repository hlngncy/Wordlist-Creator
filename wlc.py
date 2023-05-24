#!/usr/bin/env python
import time
import itertools
import os
from pyfiglet import figlet_format
from termcolor import colored

os.system("apt-get install python")
os.system("pip install pyfiglet && termcolor")
os.system("clear")



def wlc(lst):
    f = open("wordlist.txt", "w+")
    for i in lst:
        f.write(f"{i}\n")
    f.close


print((colored(figlet_format("PerWord"), color="magenta")))

print("""\033[1;33m
    --------------------------------------------------------------------
    |    Thanks for using                                               |        
    |   ----------------                                                |
    |                                                                   |
    |    1)Permutate                                                    | 
    |    2)Permutate and add to wordlist                                |
    |                                                                   |            
    --------------------------------------------------------------------
    """)
while True:
    choise = str(input("\033[1;34mPlease choose any(q to quit): "))
    if choise == "q":
        print("\033[1;32mProgram is closing... See you later!")
        time.sleep(3)
    elif choise == "2":
        things = str(input("\033[1;34mplease enter words(a,b,c): "))
        list1 = things.split(",")
        list2 = []
        counter = 1
        while (coutner < len(list1)):
            a = itertools.permutations(list1, counter + 1)
            for j in a:
                c = ''.join(j)
                list2.append(c)
            counter += 1
        wlc(list2)
        print("\033[1;32m wordlist.txt created succesfully!")
        time.sleep(3)
        break
    elif choise == "1":
        things = str(input("\033[1;34mPlease enter words(a,b,c): "))
        list1 = things.split(",")
        list2 = []
        counter = 1
        while (counter < len(list1)):
            a = itertools.permutations(list1, counter + 1)
            for j in a:
                c = ''.join(j)
                list2.append(c)
            counter += 1
        for i in list2:
            print("\033[1;36m", i)
        print("\033[1;32mAll permutation finished!")
        time.sleep(2)
        break
    else:
        print("\033[1;31mYou should enter 1, 2 or 'q'!")
        time.sleep(2)
