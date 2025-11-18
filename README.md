import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import os

# Funciones
def abrir_album(url):
    webbrowser.open(url)

def abrir_maps(lugar, categoria):
    busqueda = f"{categoria} cerca de {lugar} Corrientes"
    url = f"https://www.google.com/maps/search/{busqueda.replace(' ', '+')}"
    webbrowser.open(url)
    
def boton_moderno(parent, texto, comando):
    color_base = "#5865F2"
    color_hover = "#6B73FB"
    color_click = "#474EE5"
    shadow_color = "#2C2C54"

    sombra = tk.Frame(parent, bg=shadow_color)
    sombra.pack(side="left", padx=6, pady=6)

    btn = tk.Label(
        sombra,
        text=texto,
        bg=color_base,
        fg="white",
        font=("Helvetica", 11, "bold"),
        padx=14,
        pady=7,
        cursor="hand2",
        bd=0
    )
    btn.pack()

    def on_enter(e):
        btn.config(bg=color_hover)

    def on_leave(e):
        btn.config(bg=color_base)

    def on_click(e):
        btn.config(bg=color_click)
        btn.after(120, lambda: btn.config(bg=color_hover))
        comando()

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.bind("<Button-1>", on_click)

    return btn


# Ruta absoluta del archivo actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Datos de los álbumes
albumes = [
    {
        "nombre": "Parque 2 de Febrero, Resistencia",
        "imagen": "parque.png",
        "enlace": "https://photos.google.com/share/AF1QipMMjxajwctv0Wun0DUCqf7_RcukhdsQjdq7vYZqi3OXxd-7cM3mO7kE5MdmDtI0PA?key=cy16QzJydy1ZdEJ0NGQ5b0pSNHNTYno0d1pXdVpn"
    },
    {
        "nombre": "Paseo costanero, corrientes",
        "imagen": "costanera.png",
        "enlace": "https://photos.google.com/share/AF1QipPUb3vpEOzPO9yA04tQX1dKfRsY1NyrcwSig36dEMx1UkbPfdugWQJ0KW6dYdyDJw?key=UnJHZGdWR2tnT3BFSXNsMUo1S1Q0dmVEVExGeVB3"
    },
    {
        "nombre": "La Unidad, corrientes",
        "imagen": "unidad.png",
        "enlace": "https://photos.google.com/share/AF1QipNYx1ENMR_0ZSkVpMDug6Wu0lIBEU5wwWnCbmhPtFDpflTdnP3LXX5SGU6iOqJfng?key=ek9JTTVhUlJKcHlMWDM1aEM2RmdHTndGOWNKZzJB"
    },
    {
        "nombre": "Centro de Resistencia",
        "imagen": "centro.jpg",
        "enlace": "https://photos.google.com/share/AF1QipPmjQhg-ZZOznpj4s67Ju5qSG-MNiJ1UeLmHBNdZFHT9FbxwP502Fr6wla2Z6nqvQ?key=US0yTzN3UDkwSXVCMGw1b3FJcGNkTnJWbXpsY2FB"
    }
]



# -------------------------
# Interfaz
# -------------------------

ventana = tk.Tk()
ventana.title("Catálogo de Álbumes - Grupo 4")
ventana.configure(bg="#E8EAFE")   # Fondo suave
ventana.geometry("950x900")
ventana.title("Catálogo de Álbumes")
ventana.configure(bg="#EEE8FE")   # Fondo suave
ventana.geometry("800x800")

# Título principal
titulo = tk.Label(
    ventana,
    text="Catálogo Turístico - Resistencia / Corrientes",
    font=("Helvetica", 24, "bold"),
    bg="#E8EAFE",
    fg="#1B1B3A"
)
titulo.pack(pady=20)

# Contenedor principal
frame_albumes = tk.Frame(ventana, bg="#ECE8FE")
frame_albumes.pack(pady=10)

# -------------------------
# Mostrar álbumes
# -------------------------

for i, album in enumerate(albumes):

    ruta_imagen = os.path.join(BASE_DIR, album["imagen"])

    try:
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((300, 120))
        foto = ImageTk.PhotoImage(imagen)
    except Exception as e:
        print("Error cargando imagen:", ruta_imagen, e)
        foto = tk.PhotoImage(width=300, height=120)
        foto.put("gray60", to=(0, 0, 300, 120))

    # Marco de cada tarjeta
    marco = tk.Frame(frame_albumes, bg="#FFFFFF", bd=2, relief="ridge", padx=10, pady=10)
    marco.grid(row=i//2, column=i%2, padx=20, pady=20)

    # Imagen
    etiqueta_imagen = tk.Label(marco, image=foto, bg="white", cursor="hand2")
    etiqueta_imagen.image = foto
    etiqueta_imagen.pack()
    etiqueta_imagen.bind("<Button-1>", lambda e, url=album["enlace"]: abrir_album(url))

    # Nombre del álbum
    etiqueta_nombre = tk.Label(
        marco,
        text=album["nombre"],
        font=("Helvetica", 14, "bold"),
        bg="white",
        fg="#2C2C54"
    )
    etiqueta_nombre.pack(pady=10)

 # Botones debajo del álbum
botones_frame = tk.Frame(marco, bg="white")
botones_frame.pack(pady=5)

temas = ["Gastronomía", "Bares", "Cultura"]

for tema in temas:
    boton_moderno(
        botones_frame,
        texto=tema,
        comando=lambda t=tema, l=album["nombre"]: abrir_maps(l, t)
    )
    
# Pie de página
autor = tk.Label(
    ventana,
    text="Realizado por: Grupo 4 (Deborah Obes, Brenda Torres)",
    font=("Helvetica", 11, "italic"),
    bg="#E8EAFE",
    fg="#333"
)
autor.pack(side="bottom", pady=15)


ventana.mainloop()
