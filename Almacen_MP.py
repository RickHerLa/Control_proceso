import tkinter as tk
from tkinter import messagebox

almacen_mp = {}

def agregar_producto():
    sku = entrada_sku.get()
    producto = entrada_producto.get()
    cantidad = int(entrada_cantidad.get())

    if sku in almacen_mp:
        almacen_mp[sku]['cantidad'] += cantidad
    else:
        almacen_mp[sku] = {'producto': producto, 'cantidad': cantidad}

    messagebox.showinfo("Producto Agregado", f"Se han agregado {cantidad} unidades de {producto} ({sku})")

#Pra limpiar los campos
    entrada_sku.delete(0, tk.END)
    entrada_producto.delete(0, tk.END)
    entrada_cantidad.delete(0, tk.END)