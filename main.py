import os
import random
from sources import *


def run():
    response = int
    lives = 5 
    while(response!=0):
        os.system("clear")
        while(True):
            try:
                print("\n\tHELLOOOOO CODER!\n\n-This is the best hang man game ever.\n-Ready to play?\n")
                menu_response = int(input("Press 1 for yes or 0 for no: "))
                if(menu_response==1):
                    break
                elif(menu_response==0):
                    break
                else:
                    raise Exception
            except ValueError as ver:
                os.system("clear")
                print("-> Only numerical values pleaseee! <-")
            except Exception as ex:
                os.system("clear")
                print("-> Please choose a valid option! <-")
        if(menu_response==0):
            response = 0
        else:
            word = WORDS[random.randint(0,WORDS.__len__())]
            to_guess_l = ["_"]*word.__len__()
            while(lives!=0):
                os.system("clear")
                print("Lives: {}".format(lives))
                if(lives==5):
                    print(HANG_MAN_PARTS[5])
                elif(lives==4):
                    print(HANG_MAN_PARTS[4])
                elif(lives==3):
                    print(HANG_MAN_PARTS[3])
                elif(lives==2):
                    print(HANG_MAN_PARTS[2])
                elif(lives==1):
                    print(HANG_MAN_PARTS[1])
                else:
                    break
                to_guess_s = "".join(to_guess_l)
                print("WORD: {}".format(to_guess_s))
                if(word == to_guess_s):
                    print("\n Congrats you have win!!!")
                    input("Press any key to continue...")
                    os.system("clear")
                    break
                while(True):
                    try:
                        letter = input("GUESS: ")
                        assert not letter.isnumeric() and letter.__len__()==1
                        break
                    except AssertionError as aserr:
                        print("Remember the guess must be a single letter no words or numbers!")
                if (letter not in word):
                    lives-=1
                else:
                    for i, l in enumerate(word):
                        if l.lower() == letter.lower():
                            to_guess_l[i] = l
            if(lives==0):
                print("\n Sorry, your man is death.Try again ;)")
                input("Press any key to continue...")
                os.system("clear")

if __name__ == "__main__":
    run()