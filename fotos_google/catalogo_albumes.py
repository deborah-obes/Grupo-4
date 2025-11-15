import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import os


def abrir_album(url):
    webbrowser.open(url)

def abrir_maps(lugar, categoria):
    busqueda = f"{categoria} cerca de {lugar} Corrientes"
    url = f"https://www.google.com/maps/search/{busqueda.replace(' ', '+')}"
    webbrowser.open(url)


# Ruta absoluta del archivo actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Datos de los álbumes
albumes = [
    {
        "nombre": "Parque 2 de Febrero",
        "imagen": "parque.jpg",
        "enlace": "https://photos.google.com/share/AF1QipMdTJhWieCycslhbDi-TGHhUJpMLh5HBJtrV_SKZcx-1md86xVxDhgiH0fhORj4Ig?key=YW1sMVFMNXYxWlRISTYtQWJQdjhUU0t1YjZkVXpR"
    },
    {
        "nombre": "Plaza de los Abuelos",
        "imagen": "plaza.jpg",
        "enlace": "https://photos.google.com/share/AF1QipMiC48nkng_zHslWXoj5yHTBLOqdXovGZoqOUmUFe3e-gVcBATEs84Jfj33TmpyiQ?key=NzFLdmNfd2xGSEU1TGdiQzg5UXRqVkFaZDh0VzdR"
    },
    {
        "nombre": "Plazoleta San Martín",
        "imagen": "plazoleta.jpg",
        "enlace": "https://photos.google.com/share/AF1QipNatt5t-g5G7tHOwQBSb10A4pHR-Rw6eII8KTFZjULxgBSRDDuDGXPl4CAlKvxOmw?key=Y3NnX1JfMmY4YUw4WGpZS1FKWl9XVzY1bHN4TE1n"
    },
    {
        "nombre": "Sendero Laguna Argüello",
        "imagen": "sendero.jpg",
        "enlace": "https://photos.google.com/share/AF1QipND74qYD1MtP8fAbeYc4wA6V8dyKUVpEwIN1DzhU-pDM2VjLD2EK4Aovw-rUlHC3g?key=R1Zmc1BzV0hXV0RPd3ZOVDNMRHZINTREUHdfbFB3"
    }
]



# -------------------------
# Interfaz
# -------------------------

ventana = tk.Tk()
ventana.title("Catálogo de Álbumes - Déborah Obes")
ventana.configure(bg="#E8EAFE")   # Fondo suave
ventana.geometry("900x900")

# Título principal
titulo = tk.Label(
    ventana,
    text="Catálogo de Álbumes Fotográficos",
    font=("Helvetica", 24, "bold"),
    bg="#E8EAFE",
    fg="#1B1B3A"
)
titulo.pack(pady=20)

# Contenedor principal
frame_albumes = tk.Frame(ventana, bg="#E8EAFE")
frame_albumes.pack(pady=10)

# -------------------------
# Mostrar álbumes
# -------------------------

for i, album in enumerate(albumes):

    ruta_imagen = os.path.join(BASE_DIR, album["imagen"])

    try:
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((320, 260))
        foto = ImageTk.PhotoImage(imagen)
    except Exception as e:
        print("Error cargando imagen:", ruta_imagen, e)
        foto = tk.PhotoImage(width=320, height=260)
        foto.put("gray80", to=(0, 0, 320, 260))

    # Marco de cada tarjeta
    marco = tk.Frame(frame_albumes, bg="#FFFFFF", bd=2, relief="ridge", padx=15, pady=15)
    marco.grid(row=i//2, column=i%2, padx=25, pady=25)

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
            command=lambda t=tema, l=album["nombre"]: abrir_maps(l, t)
        )
        btn.pack(side="left", padx=5)

# Pie de página
autor = tk.Label(
    ventana,
    text="Realizado por: Déborah Obes",
    font=("Helvetica", 11, "italic"),
    bg="#E8EAFE",
    fg="#333"
)
autor.pack(side="bottom", pady=15)

ventana.mainloop()