import tkinter as tkinter

# CREAR VENTANA PRINCIPAL
ventana = tkinter.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("400x300")
ventana.config(bg="lightblue")
ventana.resizable(width=False, height=False)

# ETIQUETA DE BIENVENIDA
etiqueta_bienvenida = tkinter.Label(ventana, text="¡Hola soy Deborah Obes!", font=("Helvetica", 16), bg="lightblue")
etiqueta_bienvenida.pack(pady=20)
