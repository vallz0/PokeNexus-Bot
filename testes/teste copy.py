import pytesseract
import cv2
import pyautogui
from time import sleep

# Configure o caminho para o Tesseract
TESSERACT_PATH = "/usr/bin/tesseract"  # Ajuste o caminho conforme o seu sistema
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def check_tesseract_and_opencv():
    try:
        # Aguarde um momento antes de capturar a tela
        print("Preparando para tirar um screenshot...")
        sleep(2)
        
        # Tira um screenshot da tela inteira
        screenshot = pyautogui.screenshot()
        screenshot.save("test_screenshot.png")  # Salve a imagem temporariamente
        
        # Carregue a imagem no OpenCV
        image = cv2.imread("test_screenshot.png")
        
        # Opcional: Converta para escala de cinza para melhorar a precisão
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Use o Tesseract para reconhecer o texto
        print("Analisando texto na imagem...")
        recognized_text = pytesseract.image_to_string(gray_image)
        
        # Exibe o texto reconhecido
        print("\nTexto encontrado na imagem:")
        print(recognized_text.strip())
        
    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == "__main__":
    check_tesseract_and_opencv()
