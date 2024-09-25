import tkinter as tk
import time
import pygame
from PIL import Image, ImageTk

# Inicializar pygame para controlar el sonido
pygame.mixer.init()


def cuenta_regresiva(tiempo_en_minutos):
    tiempo_en_segundos = tiempo_en_minutos * 60
    while tiempo_en_segundos >= 0:
        mins, secs = divmod(tiempo_en_segundos, 60)
        tiempo_formateado = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=tiempo_formateado)
        root.update()
        time.sleep(1)
        tiempo_en_segundos -= 1

    # Actualizar el mensaje en la etiqueta de mensaje_final al final de la cuenta regresiva
    mensaje_final.config(text="¡El tiempo ha terminado!")
    # Reproducir sonido al finalizar la cuenta regresiva
    pygame.mixer.music.load(
        'Brucia La Terra - The Godfather.mp3')  # Asegúrate de que el archivo esté en la misma carpeta
    pygame.mixer.music.play()


def pausar_sonido():
    # Detener la reproducción del sonido
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()


# Crear la ventana principal
root = tk.Tk()
root.title("Reloj de Cuenta Regresiva")
root.geometry("400x400")

# Cargar imagen de fondo
imagen_fondo = Image.open("brucialaterra.png")  # Reemplaza con la ruta de tu imagen
imagen_fondo = imagen_fondo.resize((400, 400), Image.LANCZOS)  # Cambiado a Image.LANCZOS
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Crear un widget de etiqueta para mostrar la imagen de fondo
fondo = tk.Label(root, image=imagen_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Crear una etiqueta para mostrar el temporizador sin fondo
label = tk.Label(root, font=("Helvetica", 30), fg="red")  # Etiqueta para el temporizador
label.pack(pady=120)

# Crear una etiqueta para mostrar el mensaje final
mensaje_final = tk.Label(root, font=("Helvetica", 24), fg="red")  # Cambia el tamaño aquí
mensaje_final.pack(pady=20)

# Crear botón para pausar el sonido
boton_pausa = tk.Button(root, text="Pausar Sonido", font=("Helvetica", 14), command=pausar_sonido)
boton_pausa.pack(pady=10)

# Solicitar el tiempo en minutos
tiempo_minutos = int(input("Ingresa el tiempo en minutos para la cuenta regresiva: "))

# Iniciar la cuenta regresiva
cuenta_regresiva(tiempo_minutos)

root.mainloop()
