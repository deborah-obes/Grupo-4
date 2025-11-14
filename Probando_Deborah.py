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

# texto INFORMATIVO
texto_info = tkinter.Text(ventana, height=5, width=40, font=("Helvetica", 12))
texto_info.insert(tkinter.END, "Estoy aprendiendo a usar Tkinter para crear interfaces gráficas en Python. ¡Es muy divertido!")
texto_info.pack(pady=10)
texto_info.config(state=tkinter.DISABLED)

# Ejecutar la ventana
ventana.mainloop()
