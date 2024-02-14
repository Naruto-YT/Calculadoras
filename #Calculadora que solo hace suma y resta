#Calculadora que solo hace suma y resta

import tkinter as tk

def sumar():
    num1 = int(entry_num1.get())
    num2 = int(entry_num2.get())
    resultado = num1 + num2
    label_resultado.config(text="resultado: " + str(resultado))

app = tk.Tk()
app.title("Python Tkinter - Sumar")

label_num1 = tk.Label(text="primer numero: ")
entry_num1 = tk.Entry()

label_num2 = tk.Label(text="segundo numero: ")
entry_num2 = tk.Entry()

label_resultado = tk.Label(text= "-")

button_sumar = tk.Button(text="Sumar",command=sumar)

label_num1.pack()
entry_num1.pack()

label_num2.pack()
entry_num2.pack()

label_resultado.pack()

button_sumar.pack()

app.mainloop()
