import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import os

# -----------------------------
# FUNCIONES
# -----------------------------
def abrir_album(url):
    webbrowser.open(url)

def abrir_maps(lugar, categoria):
    busqueda = f"{categoria} cerca de {lugar} Corrientes"
    url = f"https://www.google.com/maps/search/{busqueda.replace(' ', '+')}"
    webbrowser.open(url)

def crear_boton_moderno(parent, texto, comando):
    style = ttk.Style()
    style.configure(
        "Modern.TButton",
        font=("Helvetica", 11, "bold"),
        padding=10
    )

    boton = ttk.Button(parent, text=texto, style="Modern.TButton", command=comando)
    boton.pack(side="left", padx=5)
    return boton


# -----------------------------
# CLASE PRINCIPAL
# -----------------------------
class CatalogoApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Catálogo Turístico - Resistencia / Corrientes")
        self.ventana.geometry("900x850")
        self.ventana.configure(bg="#EEE8FE")

        self.base_dir = os.path.dirname(os.path.abspath(__file__))

        self.albumes = [
            {
                "nombre": "Parque 2 de Febrero, Resistencia",
                "imagen": "parque.png",
                "enlace": "https://photos.google.com/share/AF1QipMMjxajwctv0Wun0DUCqf7_RcukhdsQjdq7vYZqi3OXxd-7cM3mO7kE5MdmDtI0PA?key=cy16QzJydy1ZdEJ0NGQ5b0pSNHNTYno0d1pXdVpn"
            },
            {
                "nombre": "Paseo costanero, Corrientes",
                "imagen": "costanera.png",
                "enlace": "https://photos.google.com/share/AF1QipPUb3vpEOzPO9yA04tQX1dKfRsY1NyrcwSig36dEMx1UkbPfdugWQJ0KW6dYdyDJw?key=UnJHZGdWR2tnT3BFSXNsMUo1S1Q0dmVEVExGeVB3"
            },
            {
                "nombre": "La Unidad, Corrientes",
                "imagen": "unidad.png",
                "enlace": "https://photos.google.com/share/AF1QipNYx1ENMR_0ZSkVpMDug6Wu0lIBEU5wwWnCbmhPtFDpflTdnP3LXX5SGU6iOqJfng?key=ek9JTTVhUlJKcHlMWDM1aEM2RmdHTndGOWNKZzJB"
            },
            {
                "nombre": "Centro de Resistencia",
                "imagen": "centro.jpg",
                "enlace": "https://photos.google.com/share/AF1QipPmjQhg-ZZOznpj4s67Ju5qSG-MNiJ1UeLmHBNdZFHT9FbxwP502Fr6wla2Z6nqvQ?key=US0yTzN3UDkwSXVCMGw1b3FJcGNkTnJWbXpsY2FB"
            }
        ]

        self.temas = ["Gastronomía", "Bares", "Cultura", "Museos", "Eventos"]

        self.crear_interfaz()

    # -----------------------------
    # INTERFAZ
    # -----------------------------
    def crear_interfaz(self):

        titulo = tk.Label(
            self.ventana,
            text="Catálogo Turístico - Resistencia / Corrientes",
            font=("Helvetica", 22, "bold"),
            fg="#1B1B3A",
            bg="#EEE8FE"
        )
        titulo.pack(pady=15)

        # Frame con scroll para álbumes
        contenedor = tk.Frame(self.ventana, bg="#EEE8FE")
        contenedor.pack(fill="both", expand=True)

        canvas = tk.Canvas(contenedor, bg="#EEE8FE", highlightthickness=0)
        scrollbar = ttk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
        self.frame_scroll = tk.Frame(canvas, bg="#EEE8FE")

        self.frame_scroll.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.frame_scroll, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Renderizar álbumes
        for i, album in enumerate(self.albumes):
            self.crear_tarjeta_album(i, album)

        # Pie
        autor = tk.Label(
            self.ventana,
            text="Realizado por: Grupo 4 (Deborah Obes, Brenda Torres)",
            font=("Helvetica", 11, "italic"),
            bg="#EEE8FE",
            fg="#333"
        )
        autor.pack(pady=10)

    # -----------------------------
    # TARJETAS DE ÁLBUM
    # -----------------------------
    def crear_tarjeta_album(self, index, album):
        ruta = os.path.join(self.base_dir, album["imagen"])

        try:
            img = Image.open(ruta).resize((320, 150))
            foto = ImageTk.PhotoImage(img)
        except:
            foto = tk.PhotoImage(width=320, height=150)

        tarjeta = tk.Frame(self.frame_scroll, bg="white", relief="raised", bd=2)
        tarjeta.grid(row=index // 2, column=index % 2, padx=20, pady=20)

        lbl_img = tk.Label(tarjeta, image=foto, bg="white", cursor="hand2")
        lbl_img.image = foto
        lbl_img.pack()
        lbl_img.bind("<Button-1>", lambda e: abrir_album(album["enlace"]))

        titulo = tk.Label(
            tarjeta,
            text=album["nombre"],
            font=("Helvetica", 14, "bold"),
            bg="white",
            fg="#1B1B3A"
        )
        titulo.pack(pady=10)

        botones = tk.Frame(tarjeta, bg="white")
        botones.pack(pady=5)

        # Crear botones temáticos
        for tema in self.temas:
            crear_boton_moderno(
                botones,
                tema,
                lambda t=tema, l=album["nombre"]: abrir_maps(l, t)
            )


# -----------------------------
# EJECUCIÓN
# -----------------------------
if __name__ == "__main__":
    ventana = tk.Tk()
    app = CatalogoApp(ventana)
    ventana.mainloop()
