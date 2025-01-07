import tkinter as tk
from tkinter import messagebox

Pokemon = []

def add_pokemon(event=None):
    pokemon = entry_pokemon.get().strip().lower().capitalize()
    if pokemon:
        listbox_pokemon.insert(tk.END, pokemon)
        Pokemon.append(pokemon)
        Pokemon.append(f"[S]{pokemon}")
        entry_pokemon.delete(0, tk.END)

def confirm_and_close():
    root.destroy()  # Fechar a janela quando o usuário confirmar

def show_capture_message():
    selected_index = listbox_pokemon.curselection()
    if selected_index:
        selected_pokemon = listbox_pokemon.get(selected_index[0])
        messagebox.showinfo("Captura!", f"{selected_pokemon} encontrado(a)!\nAgora, vá capturar!!")

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

button_capture = tk.Button(root, text="Capturar Pokémon", command=show_capture_message)
button_capture.pack()

# Iniciar o loop principal da interface gráfica
root.mainloop()

# Após fechar a janela, exibir a lista de Pokémon no console
print(Pokemon)
