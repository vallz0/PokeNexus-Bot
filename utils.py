import pytesseract
from tkinter import messagebox

IMAGE_PATHS:list = {
    "dc_screen": "Images/dc.png",
    "reload_button": "Images/reload_button.png",
    "fight_button": "Images/fight_button.png",
    "bag_button": "Images/bag_button.png",
    "run_button": "Images/run_button.png",
    "battle": "Images/battle.png",
    "pokeball_icon": "Images/pokeball_icon.png"
}

TESSERACT_PATH:str = r"C:\Users\Public\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def show_capture_message(poke):
    messagebox.showinfo("Captura!", f"{poke.capitalize()} encontrado(a)!\nAgora, vá capturar!!")
