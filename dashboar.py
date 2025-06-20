import tkinter as tk
from view.productos_view import cargar_productos
from view.agregar_view import agregar_productos

def ventana_usuario(datos):
    venta_usuario = tk.Tk()
    venta_usuario.title("Panel de Administración - Mi Tienda")
    venta_usuario.geometry("1100x600")
    venta_usuario.minsize(1000, 500)
    
    venta_usuario.grid_rowconfigure(0, weight=1)
    venta_usuario.grid_columnconfigure(1, weight=1)
    
    main_frame = tk.Frame(venta_usuario)
    main_frame.pack(fill="both", expand=True)
    
    agregar_frame = tk.Frame(main_frame, width=250, bg="white")
    agregar_frame.pack(side="left", fill="y")
    agregar_productos(agregar_frame)
    
    productos_frame = tk.Frame(main_frame, bg="#f5f7fa")
    productos_frame.pack(side="right", fill="both", expand=True)
    cargar_productos(productos_frame)
    
    venta_usuario.mainloop()