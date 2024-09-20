import tkinter as tk
import requests

# URL de la API de MockAPI
url_api = "https://66eccaed2b6cf2b89c5f4e3f.mockapi.io/IoTCarStatus"

# Función para obtener los últimos 10 registros de la API
def obtener_registros():
    try:
        # Solicitud GET a la API
        response = requests.get(url_api)
        if response.status_code == 200:
            registros = response.json()
            # Ordenar los registros por ID en orden ascendente y tomar los primeros 10
            registros_recientes = sorted(registros, key=lambda x: int(x['id']))[:10]
            mostrar_registros(registros_recientes)
        else:
            actualizar_salida(f"Error al obtener registros. Estado: {response.status_code}")
    except requests.RequestException as e:
        actualizar_salida(f"Error al conectar con la API: {e}")

# Función para mostrar los registros en el cuadro de texto
def mostrar_registros(registros):
    text_salida.config(state=tk.NORMAL)
    text_salida.delete(1.0, tk.END)  # Limpiar el texto anterior
    for registro in registros:
        text_salida.insert(tk.END, f"ID: {registro['id']} - Dirección: {registro['direccion']}\n")
    text_salida.config(state=tk.DISABLED)

# Función para actualizar el cuadro de salida con mensajes
def actualizar_salida(mensaje):
    text_salida.config(state=tk.NORMAL)
    text_salida.insert(tk.END, mensaje + "\n")
    text_salida.config(state=tk.DISABLED)
    text_salida.see(tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Visualización de Registros de IoTCarStatus")

# Ajustar tamaño de la ventana
ventana.geometry("400x400")
ventana.resizable(False, False)

# Crear cuadro de texto para mostrar los registros
text_salida = tk.Text(ventana, height=15, width=50, font=("Helvetica", 10))
text_salida.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
text_salida.config(state=tk.DISABLED)

# Crear botón para actualizar los registros
btn_actualizar = tk.Button(ventana, text="Actualizar Registros", command=obtener_registros, font=("Helvetica", 12), width=20)
btn_actualizar.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Centrar todo en la ventana
ventana.grid_columnconfigure(0, weight=1)

# Iniciar la aplicación y obtener los registros al inicio
obtener_registros()
ventana.mainloop()