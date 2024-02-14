#Calculadora con interfaz un poco mejor 

import tkinter as tk
from tkinter import messagebox

def calcular():
    op = operacion.get()
    Persona1 = float(txtN1.get())
    Persona2 = float(txtN2.get())

    if op == "sum":
        resultado = Persona1 + Persona2
    elif op == "rest":
        resultado = Persona1 - Persona2
    elif op == "mul":
        resultado = Persona1 * Persona2
    elif op == "div":
        resultado = Persona1 / Persona2
    else:
        resultado = "error"

    messagebox.showinfo("Resultado", str(resultado))

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("200x250")

operacion = tk.StringVar()
operacion.set("sum")

Persona1_label = tk.Label(ventana, text="Número 1: ")
Persona1_label.pack()

txtN1 = tk.Entry(ventana)
txtN1.pack()

Persona2_label = tk.Label(ventana, text="Número 2: ")
Persona2_label.pack()

txtN2 = tk.Entry(ventana)
txtN2.pack()

sumar_radio = tk.Radiobutton(ventana, text="Sumar", variable=operacion, value="sum")
sumar_radio.pack()

restar_radio = tk.Radiobutton(ventana, text="Restar", variable=operacion, value="rest")
restar_radio.pack()

multiplicar_radio = tk.Radiobutton(ventana, text="Multiplicar", variable=operacion, value="mul")
multiplicar_radio.pack()

btn_calcular = tk.Button(ventana, text="Calcular", command=calcular)
btn_calcular.pack()

ventana.mainloop()
