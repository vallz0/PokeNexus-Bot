
import pyautogui as py
import sys
from time import sleep as delay
import random
import pytesseract
import cv2
import re

dc_screen = "Images/dc.png"
reload_button = "Images/reload_button.png"
fight_button = "Images/fight_button.png"
bag_button = "Images/bag_button.png"
run_button = "Images/run_button.png"
Battle = "Images/battle.png"
pokeball_icon ="Images/pokeball_icon.png"
battle = "Images/Battle_Check.png"


def Check():
    try:
        
        global isBattle 
        try:
            VS = py.locateCenterOnScreen(battle,confidence=0.8)
            isBattle = True
        except:
            isBattle = False
            
        return isBattle
    except:
        print("erro no check()")
        
    
def PokeCheck():
    
    VS = py.locateCenterOnScreen(Battle,confidence=0.8)
    left,top = VS

    x = left + 48
    y = top - 30
   
    global output_file
    output_file = "Images/poke_check.png"
    screenshot = py.screenshot(region=(int(x), int(y), 180, 35))
    screenshot.save(output_file)
    imagem = cv2.imread(output_file)
   
    caminho = r"C:\Users\Public\AppData\Local\Programs\Tesseract-OCR"
    pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
    global Poke
    poke = pytesseract.image_to_string(imagem)
    Poke = poke.strip().lower()
    return Poke

PokeCheck()

