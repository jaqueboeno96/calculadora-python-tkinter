# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:09:13 2024

@author: CSP1678
"""
#Calculadora com interface gráfica tkinter:
    
import tkinter as tk

def press_key(event):
    key = event.widget.cget("text")
    if key == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, key)

# Cor
cor_fundo = "#000000"
cor_texto = "#fff"

root = tk.Tk()
root.title("Calculadora")
root.configure(bg=cor_fundo)

entry = tk.Entry(root, width=35, borderwidth=10, bg=cor_texto, fg="black")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Teclas
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

for key, row, col in buttons:
    button = tk.Button(root, text=key, padx=20, pady=10, bg=cor_fundo, fg=cor_texto)
    button.grid(row=row, column=col)
    button.bind("<Button-1>", press_key)
    button.configure(activebackground="#cccccc", activeforeground=cor_texto)

root.mainloop()
