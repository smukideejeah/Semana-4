#Programa: LAB04_EJER_42.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 23/09/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Propósito: Crear una interfaz gráfica para una librería.

from random import randint
import tkinter as tk
from tkinter import messagebox

def agregar_libro():
    nombre = entry_nombre.get().strip()
    precio = entry_precio.get().strip()
    pago = metodo_pago.get()
    code = randint(1000, 9999)

    if nombre != '' and precio != '':
        item = f"Título: {nombre}, Precio: {precio}, Pago: {pago}, ISBN: {code}"
        if item not in lista_libros.get(0, tk.END):
            lista_libros.insert(tk.END, item)
            entry_nombre.delete(0, tk.END)
            entry_precio.delete(0, tk.END)
            metodo_pago.set("Contado")
        else:
            messagebox.showwarning(
                "Error", "Ya existe un libro con ese título.")
    else:
        messagebox.showwarning(
            "Error", "Debes ingresar el nombre y precio del libro.")

def eliminar_libro():
    seleccionado = lista_libros.curselection()
    if seleccionado:
        lista_libros.delete(seleccionado)
        entry_nombre.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
        metodo_pago.set("Contado")
    else:
        messagebox.showwarning(
            "Error", "Debes seleccionar un libro para eliminar.")

def actualizar_libro():
    seleccionado = lista_libros.curselection()
    dataSelected = obtener_datos_item(lista_libros.get(seleccionado));

    nombre = entry_nombre.get().strip()
    precio = entry_precio.get().strip()
    pago = metodo_pago.get()

    if nombre != '' or precio != '':
        nombre = nombre if nombre != '' else dataSelected[0]
        precio = precio if precio != '' else dataSelected[1]
        nuevo_item = f"Título: {nombre}, Precio: {precio}, Pago: {pago}, ISBN: {dataSelected[3]}"

        if seleccionado:
            lista_libros.delete(seleccionado)
            lista_libros.insert(seleccionado, nuevo_item)
        else:
            messagebox.showwarning(
                "Error", "Debes seleccionar un libro para actualizar.")
    else:
        messagebox.showwarning(
            "Error", "Debes ingresar el nombre y precio del libro.")

def obtener_datos_item(item):
    partes = item.split(", ")
    nombre = partes[0].split(": ")[1]
    precio = partes[1].split(": ")[1]
    pago = partes[2].split(": ")[1]
    code = partes[3].split(": ")[1]
    return nombre, precio, pago, code

window = tk.Tk()
window.title("Librería UIA")

frame_data = tk.Frame(window)
frame_data.place(x = 20, y = 20)

label_nombre = tk.Label(frame_data, text="Título:")
label_nombre.grid(row = 0, column = 0)
entry_nombre = tk.Entry(frame_data)
entry_nombre.grid(row = 0, column = 1)

label_precio = tk.Label(frame_data, text="Precio:")
label_precio.grid(row=1, column=0)
entry_precio = tk.Entry(frame_data)
entry_precio.grid(row=1, column=1)

frame_data.pack()

frame_pago = tk.Frame(window)
frame_pago.place(x=20, y=70)

metodo_pago = tk.StringVar(value="Contado")

label_pago = tk.Label(frame_pago, text="Método de pago:")
label_pago.pack()

radio_contado = tk.Radiobutton(
    frame_pago, text="Contado", variable=metodo_pago, value="Contado")
radio_contado.pack()

radio_credito = tk.Radiobutton(
    frame_pago, text="Crédito", variable=metodo_pago, value="Crédito")
radio_credito.pack()
frame_pago.pack()


frame_botones = tk.Frame(window)
frame_botones.place(x=20, y=120)

boton_agregar = tk.Button(
    frame_botones, text="Agregar", command=agregar_libro)
boton_agregar.pack()

boton_eliminar = tk.Button(
    frame_botones, text="Eliminar", command=eliminar_libro)
boton_eliminar.pack()

boton_actualizar = tk.Button(
    frame_botones, text="Actualizar", command=actualizar_libro)
boton_actualizar.pack()

frame_botones.pack()

frame_lista = tk.Frame(window)
frame_lista.place(x=20, y=250)

lista_libros = tk.Listbox(frame_lista, width=70, height=10)
lista_libros.pack()
frame_lista.pack()
window.mainloop()