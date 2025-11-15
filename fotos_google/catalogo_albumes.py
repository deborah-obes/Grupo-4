import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

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

# Función para abrir el álbum
def abrir_album(url):
    webbrowser.open(url)

# Ventana principal
ventana = tk.Tk()
ventana.title("Catálogo de Álbumes - Déborah Obes")
ventana.configure(bg="lightgray")
ventana.geometry("800x800")

# Título principal
titulo = tk.Label(ventana, text="Catálogo de Álbumes Fotográficos", 
                  font=("Helvetica", 20, "bold"), bg="white", fg="#222")
titulo.pack(pady=20)

# Contenedor de álbumes
frame_albumes = tk.Frame(ventana, bg="white")
frame_albumes.pack(pady=10)

# Mostrar álbumes en una cuadrícula
for i, album in enumerate(albumes):
    try:
        imagen = Image.open(album["imagen"])
        imagen = imagen.resize((300, 250))
        foto = ImageTk.PhotoImage(imagen)
    except:
        # Si no hay imagen local, muestra un rectángulo gris
        foto = tk.PhotoImage(width=200, height=150)
        foto.put("gray80", to=(0, 0, 200, 150))
    
    # Crear marco para cada álbum
    marco = tk.Frame(frame_albumes, bg="grey", padx=20, pady=10)
    marco.grid(row=i//2, column=i%2, padx=10, pady=10)
    
    etiqueta_imagen = tk.Label(marco, image=foto, bg="white", cursor="hand2")
    etiqueta_imagen.image = foto
    etiqueta_imagen.pack()
    etiqueta_imagen.bind("<Button-1>", lambda e, url=album["enlace"]: abrir_album(url))
    
    etiqueta_nombre = tk.Label(marco, text=album["nombre"], font=("Helvetica", 12, "bold"), bg="white", fg="#333")
    etiqueta_nombre.pack(pady=5)

# Pie de autor
autor = tk.Label(ventana, text="Realizado por: Déborah Obes", 
                 font=("Helvetica", 10, "italic"), bg="white", fg="#777")
autor.pack(side="bottom", pady=10)

ventana.mainloop()
