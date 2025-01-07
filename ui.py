import tkinter as tk
from tkinter import messagebox, ttk
from bot import PokeBot

class PokeUI:
    def __init__(self):
        self.pokemon_list = []
        self.bot = PokeBot()

    def add_pokemon(self, event=None):
        pokemon_name:str = entry_pokemon.get().strip().lower()
        if pokemon_name:
            listbox_pokemon.insert(tk.END, pokemon_name)
            listbox_pokemon.insert(tk.END, f"{pokemon_name}-halloween")
            listbox_pokemon.insert(tk.END, f"[s]{pokemon_name}")
            listbox_pokemon.insert(tk.END, f"[e]{pokemon_name}")
            listbox_pokemon.insert(tk.END, f"[s][e]{pokemon_name}")
            listbox_pokemon.insert(tk.END, f"[s][e]{pokemon_name}-halloween")
            listbox_pokemon.insert(tk.END, f"[s]{pokemon_name}-halloween")
            listbox_pokemon.insert(tk.END, f"[s]{pokemon_name}-halloween")
            self.pokemon_list.append(pokemon_name)
            entry_pokemon.delete(0, tk.END)

    def confirm_and_close(self):
        root.destroy()
        print(self.pokemon_list)
        self.bot.run(self.pokemon_list)

    def show_capture_message(self, poke:str):
        messagebox.showinfo("Captura!", f"{poke.capitalize()} encontrado(a)!\nAgora, vá capturar!!")

    def start(self):
        global root, entry_pokemon, listbox_pokemon
        root = tk.Tk()
        root.title("Lista de Pokémon")
        root.geometry("400x600")
        root.configure(bg="#2E2E2E")  

        ttk.Label(root, text="Digite o nome do Pokémon:").pack(pady=(20, 5))
        entry_pokemon = ttk.Entry(root)
        entry_pokemon.pack(pady=5)
        entry_pokemon.bind("<Return>", self.add_pokemon)

        ttk.Button(root, text="Adicionar Pokémon", command=self.add_pokemon).pack(pady=(5, 5))
        listbox_pokemon = tk.Listbox(root)
        listbox_pokemon.pack(pady=(5, 20), fill=tk.BOTH, expand=True)

        ttk.Button(root, text="Confirmar", command=self.confirm_and_close).pack(pady=(5, 20))

        root.mainloop()

if __name__ == "__main__":
    poke_ui = PokeUI()
    poke_ui.start()
