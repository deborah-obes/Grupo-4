import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk
from data import PLAZAS     # Diccionario con posiciones, descripciones e imágenes de cada plaza


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Mapa Interactivo – Plazas de Resistencia")

        # CARGAMOS EL MAPA PARA SABER SU TAMAÑO REAL 
        # Esto lo usamos para que toda la app use ese mismo tamaño 
        temp_img = Image.open("assets/mapaa chaco.PNG")
        self.MAPA_W, self.MAPA_H = temp_img.size

        # AJUSTAR EL TAMAÑO DE LA VENTANA AL DEL MAPA 
        self.root.geometry(f"{self.MAPA_W}x{self.MAPA_H}")
        self.root.resizable(False, False)   # La ventana no se puede agrandar ni achicar

        # Mostrar pantalla de inicio
        self.mostrar_pantalla_inicio()


    #                     PANTALLA DE INICIO DEL PROGRAMA
    def mostrar_pantalla_inicio(self):

        # Frame principal de la pantalla de inicio
        self.inicio = tk.Frame(self.root, width=self.MAPA_W, height=self.MAPA_H)
        self.inicio.pack(fill="both", expand=True)

        # ESTABLECER IMAGEN DE FONDO
        # Se ajusta al tamaño del mapa para que NO queden bordes laterales
        self.fondo_inicio_img = Image.open("assets/carpinchoconmate.png")
        self.fondo_inicio_img = self.fondo_inicio_img.resize((self.MAPA_W, self.MAPA_H), Image.LANCZOS)
        self.fondo_inicio_tk = ImageTk.PhotoImage(self.fondo_inicio_img)

        # Colocar la imagen como fondo
        fondo_label = tk.Label(self.inicio, image=self.fondo_inicio_tk)
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

        #TEXTO PRINCIPAL 
        label = tk.Label(
            self.inicio,
            text="¿Te gustaría conocer lugares para tomar mate en Resistencia?",
            font=("Arial", 30, "bold"),
            bg="#FFFFFF",   # Fondo blanco para que se lea bien
            fg="black"
        )
        label.pack(pady=80)

        #BOTÓN PARA CONTINUAR 
        boton = tk.Button(
            self.inicio,
            text="¡Vamos!",
            font=("Arial", 22, "bold"),
            command=self.iniciar_app,   # Acción al presionar el botón
            bg="#4CAF50",
            fg="white",
            width=12,
            height=2
        )
        boton.pack(pady=40)

    
    #CAMBIAR A LA PANTALLA DEL MAPA PRINCIPAL
    def iniciar_app(self):
        self.inicio.destroy()   # Borra la pantalla de inicio
        self.cargar_mapa()      # Carga el mapa interactivo

    
    #CARGAR MAPA REAL
    def cargar_mapa(self):

        # Cargar imagen del mapa 
        self.mapa_img = Image.open("assets/mapaa chaco.PNG")
        self.mapa_tk = ImageTk.PhotoImage(self.mapa_img)

        # Crear un canvas del tamaño del mapa
        self.canvas = tk.Canvas(self.root, width=self.MAPA_W, height=self.MAPA_H)
        self.canvas.pack()

        # Colocar el mapa en el canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.mapa_tk)

        #CARGAR ICONO DE UBICACIÓN QUE SE MOSTRARÁ EN LAS PLAZAS 
        self.icono = Image.open("assets/ubicacion.png").convert("RGBA")
        self.icono = self.icono.resize((32, 32), Image.LANCZOS)
        self.icono_tk = ImageTk.PhotoImage(self.icono)

        #CREAR LOS MARCADORES DE CADA PLAZA 
        for nombre, info in PLAZAS.items():
            x, y = info["pos"]   # Coordenadas en el mapa

            # Dibujar el ícono en esas coordenadas
            marcador = self.canvas.create_image(x, y, image=self.icono_tk)

            # Hacer que al tocar un ícono se abra una ventana con la información
            self.canvas.tag_bind(
                marcador,
                "<Button-1>",
                lambda event, n=nombre: self.mostrar_info(n)
            )

    
    #VENTANA QUE MUESTRA INFO DE CADA PLAZA
    
    def mostrar_info(self, nombre):
        info = PLAZAS[nombre]   # Información de la plaza seleccionada

        ventana = Toplevel(self.root)
        ventana.title(nombre)

        # Título de la plaza
        tk.Label(ventana, text=nombre, font=("Arial", 18, "bold")).pack(pady=10)

        # Descripción
        tk.Label(
            ventana,
            text=info["desc"],
            justify="left",
            wraplength=400   #Ajusta el texto para no desbordarse
        ).pack(padx=10, pady=10)

        #Imagen asociada a la plaza
        img = Image.open(info["img"])
        img = img.resize((350, 250))
        img_tk = ImageTk.PhotoImage(img)

        tk.Label(ventana, image=img_tk).pack(pady=10)

        #Mantener referencia para que la imagen NO se borre de memoria
        ventana.image_ref = img_tk



#INICIO DEL PROGRAMA

root = tk.Tk()
app = App(root)
root.mainloop()
