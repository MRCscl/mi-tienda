import tkinter as tk
from tkinter import ttk, messagebox
from mi_sql import conectar
from view.productos_view import actualizar_productos  

def agregar_producto(nombre, precio, cantidad):
    try:
        precio = float(precio)
        cantidad = int(cantidad)
        conectar(f"INSERT INTO productos (nombre, precio, cantidad) VALUES ('{nombre}', {precio}, {cantidad})")
        return True
    except ValueError:
        messagebox.showerror("Error", "Precio debe ser número y cantidad entero")
        return False
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo agregar: {str(e)}")
        return False

def agregar_productos(ventana):
    color_fondo = "#ffffff"
    color_principal = "#6366f1"
    
    agregar_panel = tk.Frame(ventana, bg=color_fondo, width=250)
    agregar_panel.pack(side="left", fill="y", padx=10, pady=10)
    
    marco = tk.Frame(agregar_panel, bg=color_fondo, padx=15, pady=15)
    marco.pack(fill="both", expand=True)
    
    tk.Label(
        marco,
        text="AGREGAR PRODUCTO",
        font=("Segoe UI", 14, "bold"),
        bg=color_fondo,
        fg=color_principal
    ).pack(pady=10)
    
    campos = [
        {"label": "Nombre", "show": ""},
        {"label": "Precio", "show": ""},
        {"label": "Cantidad", "show": ""}
    ]
    entries = []
    
    for campo in campos:
        frame = tk.Frame(marco, bg=color_fondo)
        frame.pack(fill="x", pady=8)
        
        tk.Label(
            frame,
            text=campo["label"] + ":",
            bg=color_fondo,
            font=("Segoe UI", 10)
        ).pack(fill="x")
        
        entry = ttk.Entry(frame, font=("Segoe UI", 11))
        entry.pack(fill="x", ipady=4)
        entries.append(entry)
    
    def manejar_agregar():
        nombre = entries[0].get()
        precio = entries[1].get()
        cantidad = entries[2].get()
        
        if not all([nombre, precio, cantidad]):
            messagebox.showerror("Error", "Todos los campos son requeridos")
            return
            
        if agregar_producto(nombre, precio, cantidad):  # LLAMADA CORRECTA
            for entry in entries:
                entry.delete(0, tk.END)
            
            actualizar_productos()
            
            messagebox.showinfo("Éxito", "Producto agregado correctamente")
    
    btn_agregar = tk.Button(
        marco,
        text="AGREGAR",
        command=manejar_agregar,
        bg=color_principal,
        fg="white",
        font=("Segoe UI", 12, "bold"),
        relief="flat",
        pady=8
    )
    btn_agregar.pack(fill="x", pady=20)
    
    btn_agregar.bind("<Enter>", lambda e: btn_agregar.config(bg="#4f46e5"))
    btn_agregar.bind("<Leave>", lambda e: btn_agregar.config(bg=color_principal))