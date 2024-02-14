# Calculadora - DIVISION - MULTIP - RESTA - SUMA 

import tkinter as tk
from tkinter import messagebox

def calcular():
    P1 = int(txt1.get())
    P2 = int(txt2.get())
    suma = P1 + P2
    resta = P1 - P2
    mul = P1 * P2
    div = P1 / P2

    messagebox.showinfo("Resultado",
    "Suma: "+str(suma) +
    "\nResta: " + str(resta) +
    "\nMultiplicación: " + str(mul) +
    "\nDivisión: " + str(div))

root = tk.Tk()
root.title("Mi primera calculadora")
root.geometry("300x200")

etiqueta1 = tk.Label(root, text= "Sumar, restar, multiplicar y dividir")
txt1 = tk.Entry(root)
txt2 = tk.Entry(root)

btn_calcular = tk.Button(root, text="Calcular", command=calcular)

etiqueta1.pack()
txt1.pack()
txt2.pack()
btn_calcular.pack()

root.mainloop()
