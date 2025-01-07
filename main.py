import os
import threading
from ui import PokeUI
from time import sleep, time

def clear_console() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def periodic_clear_console(interval:int=15) -> None:
    while True:
        sleep(interval)
        clear_console()

def main() -> None:
    clear_thread = threading.Thread(target=periodic_clear_console, daemon=True)
    clear_thread.start()

    poke_ui = PokeUI()
    poke_ui.start()

if __name__ == "__main__":
    main()
    