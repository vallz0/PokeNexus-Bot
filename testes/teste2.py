import tkinter as tk
from tkinter import messagebox

Pokemon = []

def add_pokemon(event=None):
    pokemon = entry_pokemon.get().strip().lower()
    if pokemon:
        listbox_pokemon.insert(tk.END, pokemon)
        Pokemon.append(pokemon)
        entry_pokemon.delete(0, tk.END)

def confirm_and_close():
    if len(Pokemon) == 1:
        root.destroy()  # Fechar a janela se os 3 Pokémon foram adicionados
    else:
        messagebox.showwarning("Aviso", "Por favor, insira 1 Pokémon.")

# Criar a janela principal
root = tk.Tk()
root.title("Lista de Pokémon")

# Criar widgets
label_pokemon = tk.Label(root, text="Digite o nome do Pokémon:")
label_pokemon.pack()

entry_pokemon = tk.Entry(root)
entry_pokemon.pack()
entry_pokemon.bind("<Return>", add_pokemon)  # Vincular a tecla Enter ao evento de adicionar Pokémon

button_add = tk.Button(root, text="Adicionar Pokémon", command=add_pokemon)
button_add.pack()

listbox_pokemon = tk.Listbox(root)
listbox_pokemon.pack()

button_confirm = tk.Button(root, text="Confirmar", command=confirm_and_close)
button_confirm.pack()

# Iniciar o loop principal da interface gráfica
root.mainloop()

# Após fechar a janela, exibir a lista de Pokémon no console
print(Pokemon)
