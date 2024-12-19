def visualizar_producto_terminado():
    label = tk.Label(root, text="Producto Terminado Producido:", font=("Helvetica", 12))
    label.pack(pady=10)

    # Mostrar producto terminado desde la variable global `producto_terminado`
    for sku, cantidad in producto_terminado.items():
        label_producto = tk.Label(root, text=f"Producto: {sku}, Cantidad Producida: {cantidad}")
        label_producto.pack(pady=5)