import pyautogui as pyddddddddddddddddddddddddddddddddddaaaaaaaaaaaaaaaaaaaaaaaaaaaa
import sys
from time import sleep as delay
import random
import pytesseract
import cv2
import re

# 126/151 dex kanto
#24/100 dex johto

dc_screen = "Images/dc.png"
reload_button = "Images/reload_button.png"
fight_button = "Images/fight_button.png"
bag_button = "Images/bag_button.png"
run_button = "Images/run_button.png"
Battle = "Images/battle.png"
pokeball_icon ="Images/pokeball_icon.png"

Pokemon = ["Bulbasaur","Volcanion","Nidorino"]
Pokemon = [pokemon.strip().lower() for pokemon in Pokemon]
rn = random.randrange(2,3)


def Check():
    try:
        
        global isBattle 
        try:
            VS = py.locateCenterOnScreen(Battle,confidence=0.8)
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
    y = top - 15
   
    global output_file
    output_file = "Images/poke_check.png"
    screenshot = py.screenshot(region=(int(x), int(y), 180, 35))
    screenshot.save(output_file)
   


def PokeCheck2():
   
    PokeCheck()
    imagem = cv2.imread(output_file)
    caminho = r"C:\Users\Public\AppData\Local\Programs\Tesseract-OCR"
    pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
    global Poke
    poke = pytesseract.image_to_string(imagem)
    Poke = re.sub(r'[_\-,\.]', '', poke.strip().lower())

    return Poke

"""
def DC_check():
    while True:
        
        global disconnect 
        disconnect = False
        try:
            dc = py.locateCenterOnScreen(dc_screen,confidence=0.8)
            disconnect = True
            
            
        except:
            disconnect = False
            
        return disconnect
        """
    
def click(imagem_arquivo):
    try:
        imagem = py.locateCenterOnScreen(imagem_arquivo, confidence=0.8)
        
        if imagem is not None:
            
            py.click(imagem)
            
        else:
            print("Imagem não encontrada.")
    except:
        pass
    
def Move():

    py.keyDown('left')
    delay(rn)
    py.keyUp('left')
    py.keyDown('right')
    delay(rn)
    py.keyUp('right')
  
def Move2():

    py.keyDown('up')
    delay(rn)
    py.keyUp('up')
    py.keyDown('down')
    delay(rn)
    py.keyUp('down')
  
def Atk():
    
    py.press('1')
    delay(0.5)
    py.press('1')
def Reload():
    
    click(reload_button)
    delay(0.5)


def Caught():
    click(bag_button)


try:
    
    py.click(604,457)
    while True:
        
        Check()
        if isBattle == True:
            try:
                PokeCheck2()
                
                if Poke in Pokemon:
                    
                    click(bag_button)
                    print(f"{Poke} encontrado(a)!")
                    print("Agora, vá capturar!!")
                    break
            

                else:
                    Atk()
                    
                
            except:
                pass
        else: 
            Move()
    
            
except KeyboardInterrupt:
    print('\n')

