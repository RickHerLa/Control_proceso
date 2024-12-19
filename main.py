import tkinter as tk
from tkinter import ttk
from Almacen_MP import agregar_producto
from produccion import producir_producto
from Producto_Terminado import visualizar_producto_terminado
from resumen import ver_resumen

def show_menu():
    clear_window()
    label = tk.Label(root, text="Menú Principal", font=("Helvetica", 25))
    label.pack(pady=20)

#boton_almacen_mp

    boton_almacen_mp = tk.Button(root, text="Almacén de Materias Primas", width=30, command=show_almacen_mp)
    boton_almacen_mp.pack(pady=10)

    boton_produccion = tk.Button(root, text="Producción", width=30, command=show_produccion)
    boton_produccion.pack(pady=10)

    boton_producto_terminado = tk.Button(root, text="Producto Terminado", width=30, command=show_producto_terminado)
    boton_producto_terminado.pack(pady=10)

    boton_resumen = tk.Button(root, text="Resumen", width=30, command=show_resumen)
    boton_resumen.pack(pady=10)

def show_almacen_mp():
    clear_window()
    label = tk.Label(root, text="Almacén de Materias Primas", font=("Helvetica", 20))
    label.pack(pady=10)

# Entradas para agregar productos
    global entrada_sku, entrada_producto, entrada_cantidad
    tk.Label(root, text="Ingresa el SKU del producto").pack(padx=5, pady=5, anchor="center")
    entrada_sku = tk.Entry(root)
    entrada_sku.pack(pady=5)
    
    tk.Label(root, text="Ingresa que Producto es").pack(padx=5, pady=5, anchor="center")
    entrada_producto = tk.Entry(root)
    entrada_producto.pack(pady=5)
    
    tk.Label(root, text="Ingresa la cantidad").pack(padx=5, pady=5, anchor="center")
    entrada_cantidad = tk.Entry(root)
    entrada_cantidad.pack(pady=5)

    tk.Label(root, text="Ingresa las unidades del producto (Kg, litros, toneladas, etc.)").pack(padx=5, pady=5, anchor="center")
    entrada_cantidad = tk.Entry(root)
    entrada_cantidad.pack(pady=5)



    boton_agregar = tk.Button(root, text="Agregar Producto", command=agregar_producto)
    boton_agregar.pack(pady=10)

    boton_agregar = tk.Button(root, text="Volver al Menú", command=show_menu)
    boton_agregar.pack(pady=10)

def show_produccion():
    clear_window()
    label = tk.Label(root, text="Producción", font=("Helvetica", 20))
    label.pack(pady=10)

# Entradas para producción
    global entrada_producto_a_usar, entrada_cantidad_a_producir
    entrada_producto_a_usar = tk.Entry(root)
    entrada_producto_a_usar.pack(pady=5)
    entrada_cantidad_a_producir = tk.Entry(root)
    entrada_cantidad_a_producir.pack(pady=5)

    boton_producir = tk.Button(root, text="Producir Producto", command=producir_producto)
    boton_producir.pack(pady=10)

    boton_agregar = tk.Button(root, text="Volver al Menú", command=show_menu)
    boton_agregar.pack(pady=10)

def show_producto_terminado():
    clear_window()
    label = tk.Label(root, text="Producto Terminado", font=("Helvetica", 20))
    label.pack(pady=10)

# Visualizar producto terminado
    visualizar_producto_terminado()

    boton_agregar = tk.Button(root, text="Volver al Menú", command=show_menu)
    boton_agregar.pack(pady=10)

def show_resumen():
    clear_window()
    label = tk.Label(root, text="Resumen de Operaciones", font=("Helvetica", 20))
    label.pack(pady=10)

# Mostrar resumen de movimientos y producción
    ver_resumen()

    boton_agregar = tk.Button(root, text="Volver al Menú", command=show_menu)
    boton_agregar.pack(pady=10)

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de Inventarios y Producción")
root.geometry("600x600")

show_menu()

root.mainloop()
