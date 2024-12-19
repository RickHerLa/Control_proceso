def ver_resumen():
    label_resumen = tk.Label(root, text="Resumen de Movimientos y Producción", font=("Helvetica", 16))
    label_resumen.pack(pady=10)

    # Mostrar resumen de movimientos en el almacén de materias primas
    for sku, datos in almacen_mp.items():
        label = tk.Label(root, text=f"SKU: {sku}, Producto: {datos['producto']}, Cantidad: {datos['cantidad']}")
        label.pack(pady=5)

    # Mostrar resumen de productos terminados
    for sku, cantidad in producto_terminado.items():
        label = tk.Label(root, text=f"Producto Terminado: {sku}, Cantidad Producida: {cantidad}")
        label.pack(pady=5)
