import tkinter as tk
from PIL import Image, ImageTk
import random

# Lista de palabras relacionadas con arquitectura
palabras = [
    "PLANO", "LADRILLO", "COLUMNA", "ARCO", "CEMENTO", "VIGA", "LOSA", 
    "TECHO", "PARED", "PUERTA", "VENTANA", "PILAR", "CUPULA", "MURO",
    "ARQUITECTO", "EDIFICIO", "FACHADA", "CIMENTACION", "ELEVADOR", 
    "ESCALERA", "HORMIGON", "ACERO", "VIDRIO", "MADERA", "PAVIMENTO",
    "BALCON", "TERRAZA", "JARDIN", "PATIO", "SUELO","CANALETA", 
    "ACABADOS", "DIRECCION", "OBRA", "MAQUETA", "EQUIPO", "DISEÑO", 
    "ESPACIO", "FUNCIONAL", "ESTRUCTURA", "SOSTENIBLE", "URBANISMO", 
    "REHABILITACION", "PATRIMONIO", "MODERNO", "CLASICO", "CONTEMPORANEO", 
    "RENOVACION", "PLANIFICACION", "ZONIFICACION", "INFRAESTRUCTURA", 
    "SOSTENIBILIDAD", "ERGONOMIA", "ILUMINACION"
]

# Elegir una palabra al azar
palabra_secreta = random.choice(palabras)
letras_adivinadas = []
intentos = 5
letras_falladas = []

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ahorcado Arquitectura")
ventana.geometry("600x400")

# Cargar imagen de fondo
imagen_fondo = Image.open("fondo_ahorcado.jpg")
imagen_fondo = imagen_fondo.resize((600, 400))
fondo = ImageTk.PhotoImage(imagen_fondo)

# Mostrar imagen de fondo
fondo_label = tk.Label(ventana, image=fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Función para mostrar la palabra con guiones
def mostrar_palabra():
    palabra_mostrada = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "
    return palabra_mostrada

# Función para adivinar
def adivinar():
    global intentos
    letra = entrada.get().upper()
    entrada.delete(0, tk.END)

    if letra in palabra_secreta and letra not in letras_adivinadas:
        letras_adivinadas.append(letra)
    elif letra not in palabra_secreta and letra not in letras_falladas:
        letras_falladas.append(letra)
        intentos -= 1

    # Actualizar etiquetas
    etiqueta_palabra.config(text=mostrar_palabra())
    etiqueta_intentos.config(text=f"Intentos que te quedan: {intentos}")
    etiqueta_falladas.config(text=f"Letras falladas: {' '.join(letras_falladas)}")

    # Comprobar victoria o derrota
    if all(letra in letras_adivinadas for letra in palabra_secreta):
        etiqueta_resultado.config(text="¡Ganaste! 🎉", fg="green")
        boton_adivinar.config(state="disabled")
    elif intentos == 0:
        etiqueta_resultado.config(text=f"Perdiste 😢 La palabra era: {palabra_secreta}", fg="red")
        boton_adivinar.config(state="disabled")

# Etiquetas del juego
etiqueta_titulo = tk.Label(ventana, text="🏛️ Ahorcado Arquitectura 🧱", font=("Arial", 15, "bold"), bg="white")
etiqueta_titulo.place(relx=0.5, y=40, anchor="center")

etiqueta_palabra = tk.Label(ventana, text=mostrar_palabra(), font=("Courier", 24, "bold"), bg="white", fg="black")
etiqueta_palabra.place(relx=0.5, rely=0.3, anchor="center")

etiqueta_intentos = tk.Label(ventana, text=f"Intentos que te quedan: {intentos}", font=("Arial", 14), bg="yellow")
etiqueta_intentos.place(relx=0.5, rely=0.45, anchor="center")

etiqueta_falladas = tk.Label(ventana, text="Letras falladas:", font=("Arial", 12, "italic"), bg="white", fg="red")
etiqueta_falladas.place(relx=0.5, rely=0.55, anchor="center")

# Entrada de texto y botón
tk.Label(ventana, text="Tirá una letra:", font=("Arial", 14), bg="white").place(relx=0.4, rely=0.65, anchor="center")
entrada = tk.Entry(ventana, width=3, font=("Arial", 18))
entrada.place(relx=0.55, rely=0.65, anchor="center")

boton_adivinar = tk.Button(ventana, text="¡Adivinar!", font=("Arial", 12, "bold"), bg="green", fg="white", command=adivinar)
boton_adivinar.place(relx=0.55, rely=0.75, anchor="center")

# Resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 16, "bold"), bg="white")
etiqueta_resultado.place(relx=0.5, rely=0.85, anchor="center")

# Ejecutar ventana

ventana.mainloop()
