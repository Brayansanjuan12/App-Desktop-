import tkinter as tk
import requests

# URL de la API de mockapi
url_api = "https://66eccaed2b6cf2b89c5f4e3f.mockapi.io/IoTCarStatus"

# Función para enviar el estado a la API
def enviar_a_api(direccion):
    datos = {"direccion": direccion}
    try:
        response = requests.post(url_api, json=datos)
        if response.status_code == 201:
            mensaje = f"Dirección '{direccion}' enviada correctamente."
            print(mensaje)
            actualizar_salida(mensaje)
        else:
            mensaje = f"Error al enviar la dirección '{direccion}'. Estado: {response.status_code}"
            print(mensaje)
            actualizar_salida(mensaje)
    except requests.RequestException as e:
        mensaje = f"Error al conectar con la API: {e}"
        print(mensaje)
        actualizar_salida(mensaje)

# Función para actualizar la descripción en la interfaz y enviar a la API
def actualizar_direccion(direccion):
    label_direccion.config(text=f"Dirección: {direccion}")
    enviar_a_api(direccion)

# Función para actualizar el cuadro de salida con la descripción
def actualizar_salida(mensaje):
    text_salida.config(state=tk.NORMAL)
    text_salida.insert(tk.END, mensaje + "\n")  # Agregar el nuevo mensaje sin borrar el anterior
    text_salida.config(state=tk.DISABLED)
    text_salida.see(tk.END)  # Desplazar el cuadro de texto al final para mostrar el último registro

# Funciones para los botones
def adelante():
    actualizar_direccion("adelante")

def atras():
    actualizar_direccion("atras")

def izquierda():
    actualizar_direccion("izquierda")

def derecha():
    actualizar_direccion("derecha")

def alto():
    actualizar_direccion("alto")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Control de Carro IoT")

# Ajustar tamaño de la ventana
ventana.geometry("400x500")
ventana.resizable(False, False)

# Crear etiqueta para mostrar la dirección actual
label_direccion = tk.Label(ventana, text="Dirección: ", font=("Helvetica", 14))
label_direccion.grid(row=0, column=0, columnspan=3, pady=10)

# Crear cuadro de texto para mostrar la salida de la API
text_salida = tk.Text(ventana, height=8, width=40, font=("Helvetica", 10))
text_salida.grid(row=5, column=0, columnspan=3, padx=10, pady=20)
text_salida.config(state=tk.DISABLED)  # Desactivar la edición del texto

# Crear botones con estilo
btn_style = {"font": ("Helvetica", 12), "width": 10, "height": 2, "bg": "lightblue"}

btn_adelante = tk.Button(ventana, text="Adelante", command=adelante, **btn_style)
btn_atras = tk.Button(ventana, text="Atrás", command=atras, **btn_style)
btn_izquierda = tk.Button(ventana, text="Izquierda", command=izquierda, **btn_style)
btn_derecha = tk.Button(ventana, text="Derecha", command=derecha, **btn_style)
btn_alto = tk.Button(ventana, text="Alto", command=alto, **btn_style)

# Posicionar los botones en la ventana de forma centrada
btn_adelante.grid(row=1, column=1, pady=10)
btn_izquierda.grid(row=2, column=0, padx=10, pady=10)
btn_alto.grid(row=2, column=1, padx=10, pady=10)  # El botón "Alto" en el centro
btn_derecha.grid(row=2, column=2, padx=10, pady=10)
btn_atras.grid(row=3, column=1, pady=10)  # El botón "Atrás" debajo del botón "Alto"

# Centrar todo en la ventana
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_columnconfigure(2, weight=1)

# Iniciar la aplicación
ventana.mainloop()