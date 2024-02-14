#Interfaz de calculadora mas avanzado

import tkinter as tk
from tkinter import messagebox, simpledialog

ventana = tk.Tk()
ventana.title("Menú principal")

def salir():
    resp = messagebox.askquestion("Salir", "¿Desea salir?")
    if resp == 'yes':
        ventana.destroy()

def acerca_de():
    messagebox.showinfo("Acerca de", "Desarrollado por Palacio")

def restar():
    num1 = simpledialog.askinteger("Resta", "Ingresa el primer valor:")
    num2 = simpledialog.askinteger("Resta", "Ingresa el segundo valor:")
    resta = num1 - num2
    messagebox.showinfo("Resultado", f"La resta es {resta}")

def ventana_sumar():
    v1 = tk.Toplevel(ventana)
    v1.title("Sumar")
    titulo = tk.Label(v1, text="Sumar dos números")
    v1.geometry("250x250")
    def sumar(): 
        n1 = int(text1.get())
        n2 = int(text2.get())
        suma = n1 + n2
        messagebox.showinfo("Resultado", f"La suma es {suma}")
    text1 = tk.Entry(v1)
    text2 = tk.Entry(v1)
    btn1 = tk.Button(v1, text="Sumar", command=sumar)
    titulo.pack()
    text1.pack()
    text2.pack()
    btn1.pack()

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_inicio = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
menu_inicio.add_command(label="Cerrar", command=salir)

menu_operaciones = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Operaciones", menu=menu_operaciones)
menu_operaciones.add_command(label="Sumar", command=ventana_sumar)
menu_operaciones.add_command(label="Resta", command=restar)

menu_ayuda = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)

ventana.mainloop()
