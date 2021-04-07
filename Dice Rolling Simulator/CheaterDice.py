# Customizable dice play

import random

x= "y"
nos=[1,2,3,4,5,6]


def dice_fun(no):
        if no == 1: 
            print("[-----]") 
            print("[-----]") 
            print("[  0  ]") 
            print("[-----]") 
            print("[-----]") 
        if no == 2: 
            print("[-----]") 
            print("[-0---]") 
            print("[-----]") 
            print("[---0-]") 
            print("[-----]") 
        if no == 3: 
            print("[-----]") 
            print("[--0--]") 
            print("[--0--]") 
            print("[--0--]") 
            print("[-----]") 
        if no == 4: 
            print("[-----]") 
            print("[-0-0-]") 
            print("[-----]") 
            print("[-0-0-]") 
            print("[-----]") 
        if no == 5: 
            print("[-----]") 
            print("[-0-0-]") 
            print("[--0--]") 
            print("[-0-0-]") 
            print("[-----]") 
        if no == 6: 
            print("[-----]") 
            print("[-0-0-]") 
            print("[-0-0-]") 
            print("[-0-0-]") 
            print("[-----]") 


if __name__ == "__main__":
    dice_no = int(input("With How many dices you want to Play?\n"))
    while x=="y":
        custom=input("Whether you wanted to have a customizable dice?,if Yes then type y else n")
        
        if custom=="y":
            number=int(input("If Yes then type , of which number?"))
            if number==1 :nos=[1,1,1,2,3,4,5,6]
            if number==2 :nos=[1,2,2,2,3,4,5,6]
            if number==3 :nos=[1,2,3,3,3,4,5,6]
            if number==4 :nos=[1,2,3,4,4,4,5,6]
            if number==5 :nos=[1,2,3,4,5,5,5,6]
            if number==6 :nos=[1,2,3,4,5,6,6,6]
        
        for i in range( dice_no):
            print(dice_fun(random.choice(nos)))
        x=input("type \'y\' for rolling again")
    