import pyautogui as py
from time import sleep as delay
import random
import pytesseract
import cv2
from utils import show_capture_message, IMAGE_PATHS, TESSERACT_PATH


class PokeBot:
    def __init__(self):
        self.pokemon_list:list = []
        self.rn:float = random.uniform(2, 3) 

    def check_battle(self) -> bool:
        """Verifica se a batalha está ativa."""
        try:
            return py.locateCenterOnScreen(IMAGE_PATHS["battle"], confidence=0.8) is not None
        except py.ImageNotFoundException:
            print("[Erro] Imagem da batalha não encontrada na tela.")
            return False
        except Exception as e:
            print(f"[Erro] Falha ao verificar batalha: {e}")
            return False

    def poke_check(self):
        """Captura o nome do Pokémon na batalha."""
        try:
            battle_location = py.locateCenterOnScreen(IMAGE_PATHS["battle"], confidence=0.8)
            if not battle_location:
                print("[Info] Nenhuma batalha detectada. Continuando...")
                return None

            x, y = battle_location
            screenshot = py.screenshot(region=(int(x + 48), int(y - 15), 350, 35))
            temp_image_path:str = "Images/temp_poke_check.png"
            screenshot.save(temp_image_path)

            image = cv2.imread(temp_image_path)
            pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
            poke = pytesseract.image_to_string(image).strip().lower()
            print(f"[Info] Pokémon detectado: {poke}")
            return poke
        except py.ImageNotFoundException:
            print("[Erro] Imagem não encontrada para detecção do Pokémon.")
            return None
        except Exception as e:
            print(f"[Erro] Falha ao capturar Pokémon: {e}")
            return None

    def move(self):
        """Movimento horizontal."""
        py.keyDown('a')
        delay(self.rn)
        py.keyUp('a')
        delay(0.5)
        py.keyDown('d')
        delay(self.rn)
        py.keyUp('d')

    def move2(self):
        """Movimento vertical."""
        py.keyDown('w')
        delay(self.rn)
        py.keyUp('w')
        delay(0.5)
        py.keyDown('s')
        delay(self.rn)
        py.keyUp('s')

    def attack(self):
        """Ataca o inimigo."""
        py.press('1')
        delay(0.5)
        py.press('1')

    def caught(self):
        """Captura o Pokémon."""
        py.press('2')

    def run(self, pokemon_list):
        """Executa o bot."""
        self.pokemon_list = pokemon_list
        print("[Info] Iniciando o bot...")
        try:
            while True:
                if self.check_battle():
                    poke = self.poke_check()
                    if poke and poke in self.pokemon_list:
                        print(f"[Captura] {poke.capitalize()} encontrado! Capturando...")
                        self.caught()
                        delay(0.5)
                        show_capture_message(poke)
                        break
                    else:
                        print(f"[Batalha] {poke.capitalize() if poke else 'Desconhecido'} não está na lista. Atacando...")
                        delay(0.5)
                        self.attack()
                        delay(0.5)
                else:
                    print("[Info] Nenhuma batalha detectada. Movendo...")
                    self.move()
        except KeyboardInterrupt:
            print("\n[Info] Bot interrompido pelo usuário.")
