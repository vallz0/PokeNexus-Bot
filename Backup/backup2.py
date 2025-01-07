# POKE NEXUS BOT WITH PYTHON 
#-------------------------------------
# LIBS
#-------------------------------------
import pyautogui as py
from time import sleep as delay
import random
import pytesseract
import cv2
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#-------------------------------------
# CONSTANTS
#-------------------------------------

IMAGE_PATHS = {
    "dc_screen": "Images/dc.png",
    "reload_button": "Images/reload_button.png",
    "fight_button": "Images/fight_button.png",
    "bag_button": "Images/bag_button.png",
    "run_button": "Images/run_button.png",
    "battle": "Images/battle.png",
    "pokeball_icon": "Images/pokeball_icon.png"
}
TESSERACT_PATH = r"C:\Users\Public\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

#-------------------------------------
# GLOBAL VARIABLES
#-------------------------------------
pokemon_list = []
rn = random.randrange(2,3)

#-------------------------------------
# UI FUNCTION
#-------------------------------------
def add_pokemon(event=None):

    pokemon_name = entry_pokemon.get().strip().lower()
    if pokemon_name:
        listbox_pokemon.insert(tk.END, pokemon_name)
        listbox_pokemon.insert(tk.END, f"{pokemon_name}-halloween")
        listbox_pokemon.insert(tk.END, f"[s]{pokemon_name}")
        listbox_pokemon.insert(tk.END, f"[e]{pokemon_name}")
        listbox_pokemon.insert(tk.END, f"[s][e]{pokemon_name}")
        listbox_pokemon.insert(tk.END, f"[s][e]{pokemon_name}-halloween")
        listbox_pokemon.insert(tk.END, f"[s]{pokemon_name}-halloween")
        listbox_pokemon.insert(tk.END, f"[s]{pokemon_name}-halloween")
        pokemon_list.append(pokemon_name)
        entry_pokemon.delete(0, tk.END)

def confirm_and_close():
    root.destroy()
    print(pokemon_list)

def show_capture_message(poke):
    messagebox.showinfo("Captura!", f"{poke.capitalize()} encontrado(a)!\nAgora, vá capturar!!")

root = tk.Tk()
root.title("Lista de Pokémon")
root.geometry("400x600")
root.configure(bg="#2E2E2E")  

#-------------------------------------
# CONFIG UI
#-------------------------------------
style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", background="#2E2E2E", foreground="white", font=("Helvetica", 12))
style.configure("TEntry", fieldbackground="#3E3E3E", foreground="white", font=("Helvetica", 12))
style.configure("TButton", background="#3E3E3E", foreground="white", borderwidth=0)
style.map("TButton", background=[('active', '#4E4E4E')])
style.configure("TListbox", background="#3E3E3E", foreground="white", font=("Helvetica", 12))

ttk.Label(root, text="Digite o nome do Pokémon:").pack(pady=(20, 5))
entry_pokemon = ttk.Entry(root)
entry_pokemon.pack(pady=5)
entry_pokemon.bind("<Return>", add_pokemon)

ttk.Button(root, text="Adicionar Pokémon", command=add_pokemon).pack(pady=(5, 5))
listbox_pokemon = tk.Listbox(root)
listbox_pokemon.pack(pady=(5, 20), fill=tk.BOTH, expand=True)

ttk.Button(root, text="Confirmar", command=confirm_and_close).pack(pady=(5, 20))

root.mainloop()

#-------------------------------------
# BOT LOGIC FUNCTIONS
#-------------------------------------
def check_battle():
    try:
        return py.locateCenterOnScreen(IMAGE_PATHS["battle"], confidence=0.8) is not None
    except Exception as e:
       # print(f"Error in check_battle: {e}")
        return False

def poke_check():
    battle_location = py.locateCenterOnScreen(IMAGE_PATHS["battle"], confidence=0.8)
    if battle_location:
        x, y = battle_location
        screenshot = py.screenshot(region=(int(x + 48), int(y - 15), 350, 35))
        screenshot.save("Images/poke_check.png")
        image = cv2.imread("Images/poke_check.png")
        
        pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
        poke = pytesseract.image_to_string(image).strip().lower()
        return poke
    return None

def Move():
    py.keyDown('a')
    delay(rn)
    py.keyUp('a')
    delay(0.5)
    py.keyDown('d')
    delay(rn)
    py.keyUp('d')

def Move2():
    py.keyDown('w')
    delay(rn)
    py.keyUp('w')
    delay(0.5)
    py.keyDown('s')
    delay(rn)
    py.keyUp('s')

def attack():
    py.press('1')
    delay(0.5)
    py.press('1')

def caught():
    py.press('2')
    

#-------------------------------------
# MAIN LOOP
#-------------------------------------
try:

    while True:
        if check_battle():
            poke = poke_check()
            if poke in pokemon_list:
                caught()
                delay(0.5)
                show_capture_message(poke)
                break
            else:
                delay(0.5)
                attack()
                delay(0.5)
        else:
            Move() 
except KeyboardInterrupt:
    print('\nGame interrupted.')


#-------------------------------------
# THIS SCRIPT IS MADE BY VALLZ ;)
# DISCORD: vallzk
#-------------------------------------