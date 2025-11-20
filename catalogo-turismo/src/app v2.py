"""
Catálogo turístico interactivo con Tkinter.
Muestra álbumes de fotos y enlaces a búsquedas en Google Maps.
"""

import os
import webbrowser
import tkinter as tk
from PIL import Image, ImageTk


# Funciones
def abrir_album(url: str) -> None:
    webbrowser.open(url)


def abrir_maps(lugar: str, categoria: str) -> None:
    busqueda = f"{categoria} cerca de {lugar} Corrientes"
    url = f"https://www.google.com/maps/search/{busqueda.replace(' ', '+')}"
    webbrowser.open(url)


# Ruta absoluta del archivo actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "..", "images")

# Datos de los álbumes
albumes = [
    {
        "nombre": "Parque 2 de Febrero, Resistencia",
        "imagen": "parque.png",
        "enlace":
            "https://photos.google.com/share/"
            "AF1QipMMjxajwctv0Wun0DUCqf7_RcukhdsQjdq7vYZqi3OXxd-7cM3mO7kE5MdmDtI0PA"
            "?key=cy16QzJydy1ZdEJ0NGQ5b0pSNHNTYno0d1pXdVpn"
    },
    {
        "nombre": "Paseo costanero, corrientes",
        "imagen": "costanera.png",
        "enlace":
            "https://photos.google.com/share/"
            "AF1QipPUb3vpEOzPO9yA04tQX1dKfRsY1NyrcwSig36dEMx1UkbPfdugWQJ0KW6dYdyDJw"
            "?key=UnJHZGdWR2tnT3BFSXNsMUo1S1Q0dmVEVExGeVB3"
    },
    {
        "nombre": "La Unidad, corrientes",
        "imagen": "unidad.png",
        "enlace":
            "https://photos.google.com/share/"
            "AF1QipNYx1ENMR_0ZSkVpMDug6Wu0lIBEU5wwWnCbmhPtFDpflTdnP3LXX5SGU6iOqJfng"
            "?key=ek9JTTVhUlJKcHlMWDM1aEM2RmdHTndGOWNKZzJB"
    },
    {
        "nombre": "Centro de Resistencia",
        "imagen": "centro.jpg",
        "enlace":
            "https://photos.google.com/share/"
            "AF1QipPmjQhg-ZZOznpj4s67Ju5qSG-MNiJ1UeLmHBNdZFHT9FbxwP502Fr6wla2Z6nqvQ"
            "?key=US0yTzN3UDkwSXVCMGw1b3FJcGNkTnJWbXpsY2FB"
    },
]


# ------------------------
# CATALOG0
# ------------------------

def cargar_catalogo():
    ventana = tk.Tk()
    ventana.title("Catálogo de Álbumes - Grupo 4")
    ventana.configure(bg="#E8EAFE")
    ventana.geometry("950x900")
    ventana.configure(bg="#EEE8FE")
    ventana.geometry("800x800")

    titulo = tk.Label(
        ventana,
        text="Catálogo Turístico - Resistencia / Corrientes",
        font=("Helvetica", 24, "bold"),
        bg="#E8EAFE",
        fg="#1B1B3A",
    )
    titulo.pack(pady=20)

    frame_albumes = tk.Frame(ventana, bg="#ECE8FE")
    frame_albumes.pack(pady=10)

    for i, album in enumerate(albumes):
        ruta_imagen = os.path.join(IMAGES_DIR, album["imagen"])

        try:
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((300, 120))
            foto = ImageTk.PhotoImage(imagen)
        except OSError:
            foto = tk.PhotoImage(width=300, height=120)
            foto.put("gray60", to=(0, 0, 300, 120))

        marco = tk.Frame(frame_albumes, bg="#FFFFFF", bd=2, relief="ridge", padx=10, pady=10)
        marco.grid(row=i // 2, column=i % 2, padx=20, pady=20)

        etiqueta_imagen = tk.Label(marco, image=foto, bg="white", cursor="hand2")
        etiqueta_imagen.image = foto
        etiqueta_imagen.pack()
        etiqueta_imagen.bind("<Button-1>", lambda e, url=album["enlace"]: abrir_album(url))

        etiqueta_nombre = tk.Label(
            marco,
            text=album["nombre"],
            font=("Helvetica", 14, "bold"),
            bg="white",
            fg="#2C2C54",
        )
        etiqueta_nombre.pack(pady=10)

        botones_frame = tk.Frame(marco, bg="white")
        botones_frame.pack(pady=5)

        temas = ["Gastronomía", "Bares", "Cultura"]
        for tema in temas:
            btn = tk.Button(
                botones_frame,
                text=tema,
                font=("Helvetica", 10),
                bg="#DDE3FF",
                fg="#222",
                relief="raised",
                padx=10,
                pady=3,
                cursor="hand2",
                command=lambda t=tema, l=album["nombre"]: abrir_maps(l, t),
            )
            btn.pack(side="left", padx=5)

    autor = tk.Label(
        ventana,
        text="Realizado por: Grupo 4 (Deborah Obes, Brenda Torres, Argüello Luis Mathias, Chorvat Felipe)",
        font=("Helvetica", 11, "italic"),
        bg="#E8EAFE",
        fg="#333",
    )
    autor.pack(side="bottom", pady=15)

    ventana.mainloop()



def abrir_catalogo_desde_inicio():
    inicio.destroy()
    cargar_catalogo()


inicio = tk.Tk()
inicio.title("Bienvenido")
inicio.geometry("750x500")

# Fondo
ruta_fondo = os.path.join(IMAGES_DIR, "inicio.jpg")
img_fondo = Image.open(ruta_fondo)
img_fondo = img_fondo.resize((750, 500))
fondo = ImageTk.PhotoImage(img_fondo)

label_fondo = tk.Label(inicio, image=fondo)
label_fondo.image = fondo
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Título sobre imagen
titulo_inicio = tk.Label(
    inicio,
    text="¿Sin ideas que hacer en Chaco - Corrientes?",
    font=("Arial", 26, "bold"),
    bg="#000000",
    fg="white"
)
titulo_inicio.pack(pady=40)

subtitulo = tk.Label(
    inicio,
    text="Descubrí los mejores lugares para visitar",
    font=("Arial", 15),
    bg="#000000",
    fg="white"
)
subtitulo.pack()

# Botón "Entrar"
boton_explorar = tk.Button(
    inicio,
    text="Explorar Catálogo",
    font=("Arial", 15, "bold"),
    width=22,
    bg="#C5B4E3",
    relief="raised",
    command=abrir_catalogo_desde_inicio
)
boton_explorar.pack(pady=45)

inicio.mainloop()
