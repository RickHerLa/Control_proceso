from tkinter import messagebox
from Almacen_MP import almacen_mp

def producir_producto():
    sku = entrada_producto_a_usar.get()
    cantidad_a_producir = int(entrada_cantidad_a_producir.get())

    if sku not in almacen_mp:
        messagebox.showerror("Error", "El SKU no está en el almacén.")
        return

    if almacen_mp[sku]['cantidad'] < cantidad_a_producir:
        messagebox.showerror("Error", "No hay suficiente materia prima para la producción.")
        return

    almacen_mp[sku]['cantidad'] -= cantidad_a_producir

#     Actualizar el Producto Terminado
    if sku in producto_terminado:
        producto_terminado[sku] += cantidad_a_producir
    else:
        producto_terminado[sku] = cantidad_a_producir

    messagebox.showinfo("Producción Completa", f"Se han producido {cantidad_a_producir} unidades utilizando {sku}.")

    # Para limpiar los campos
    entrada_producto_a_usar.delete(0, tk.END)
    entrada_cantidad_a_producir.delete(0, tk.END)