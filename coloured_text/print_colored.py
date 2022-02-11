import colorama
from colorama import Fore, Back, Style
import random

colorama.init(autoreset=True)
FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]

def col_picker_fore():
    return random.choice(FORES)

def col_picker_Back():
    return random.choice(BACKS)

def check_color(col,type):
    colours={'BLACK':0,'RED':1,'GREEN':2,'YELLOW':3,'BLUE':4,'MAGENTA':5,'CYAN':6,'WHITE':7}
    if type=='fore' and col in colours.keys() :
        return FORES[colours[col]]
    elif type=='back' and col in colours.keys():
        return BACKS[colours[col]]
    else:
        return False

def change_color():
    while True:
        col_fore=''
        col_back=''
        choice = input("Enter y for changing colour and any other key to quit: ").lower()
        if choice=='y':
            ch_fore = input("Enter y to enter a text colour and anyother key for a random colour: ")
            if ch_fore=='y':
                col_fore=input("Enter the text colour: ").upper()
                col_fore = check_color(col_fore,'fore')
                if col_fore == False:
                    print("Enter a valid colour")
                    break
            else:
                col_fore = col_picker_fore()
            ch_back = input("Enter y to enter a background colour and anyother key for a random colour: ")
            if ch_back=='y':
                col_back=input("Enter the background colour: ").upper()
                col_back = check_color(col_back,'back')
                if col_back == False:
                    print("Enter a valid colour")
                    break
            else:
                col_back = col_picker_Back()
            inp = input("Enter the text: ")
            print(f"{col_fore}{col_back}"+inp)
        else:
            break

change_color()