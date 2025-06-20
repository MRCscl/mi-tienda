import tkinter as tk
from tkinter import ttk
from mi_sql import conectar

productos_panel = None
canvas = None
frame_interno = None

def actualizar_productos():
    global frame_interno
    
    for widget in frame_interno.winfo_children():
        widget.destroy()
    
    productos = conectar("SELECT nombre, precio, cantidad FROM productos ORDER BY id DESC")
    
    for index, producto in enumerate(productos):
        nombre, precio, cantidad = producto
        
        card = tk.Frame(
            frame_interno, 
            bg="#ffffff", 
            bd=0,
            highlightbackground="#e5e7eb",
            highlightthickness=1,
            padx=15,
            pady=15
        )
        
        tk.Label(
            card,
            text=nombre,
            bg="#ffffff",
            fg="#111827",
            font=("Segoe UI", 12, "bold"),
            anchor="w"
        ).pack(fill="x", pady=(0,5))
        
        detalles_frame = tk.Frame(card, bg="#ffffff")
        detalles_frame.pack(fill="x")
        
        tk.Label(
            detalles_frame,
            text=f"${precio:.2f}",
            bg="#ffffff",
            fg="#4f46e5",
            font=("Segoe UI", 11, "bold"),
            anchor="w"
        ).pack(side="left", padx=(0,15))
        
        tk.Label(
            detalles_frame,
            text=f"Stock: {cantidad}",
            bg="#ffffff",
            fg="#6b7280",
            font=("Segoe UI", 10),
            anchor="w"
        ).pack(side="left")
        
        fila = index // 3  # 3 columnas
        columna = index % 3
        card.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")
        
        frame_interno.grid_columnconfigure(columna, weight=1)
    
    for i in range((len(productos) + 2) // 3):
        frame_interno.grid_rowconfigure(i, weight=1)

def cargar_productos(ventana):
    global productos_panel, canvas, frame_interno
    
    productos_panel = tk.Frame(ventana, bg="#f5f7fa", width=800, height=500)
    productos_panel.place(x=220, y=0)

    tk.Label(
        productos_panel,
        text="Inventario de Productos",
        bg="#f5f7fa",
        fg="#1f2937",
        font=("Segoe UI", 14, "bold"),
        anchor="w",
        padx=20,
        pady=15
    ).place(x=0, y=0, width=800)
    
    canvas = tk.Canvas(productos_panel, bg="#f5f7fa", bd=0, highlightthickness=0, width=760, height=430)
    scrollbar = ttk.Scrollbar(productos_panel, orient="vertical", command=canvas.yview)
    scrollbar.place(x=780, y=50, height=430)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.place(x=20, y=50)

    frame_interno = tk.Frame(canvas, bg="#f5f7fa", padx=5, pady=5)
    canvas.create_window((0, 0), window=frame_interno, anchor="nw")

    for i in range(3):  
        frame_interno.grid_columnconfigure(i, weight=1, uniform="cols")
    
    def ajustar_ancho(event):
        canvas.itemconfig("all", width=event.width-20)
    canvas.bind("<Configure>", ajustar_ancho)

    frame_interno.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    actualizar_productos()