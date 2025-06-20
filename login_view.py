import tkinter as tk
from tkinter import ttk, messagebox
from mi_sql import conectar
from view.dashboar import ventana_usuario

def cargar_login(ventana):
    color_fondo = "#f8fafc"
    color_principal = "#6366f1"
    color_secundario = "#4f46e5"
    color_texto = "#1e293b"
    color_borde = "#e2e8f0"
    
    login_panel = tk.Frame(ventana, bg=color_fondo)
    login_panel.pack(fill="both", expand=True)
    
    marco_central = tk.Frame(login_panel, bg="white", bd=0, highlightthickness=0, 
                           padx=40, pady=50, relief="flat")
    marco_central.place(relx=0.5, rely=0.5, anchor="center")
    
    tk.Label(
        marco_central,
        text="🔐 MI TIENDA",
        font=("Segoe UI", 24, "bold"),
        bg="white",
        fg=color_principal,
        pady=10
    ).pack()
    
    tk.Label(
        marco_central,
        text="Inicia sesión para continuar",
        font=("Segoe UI", 11),
        bg="white",
        fg="#64748b",
        pady=0
    ).pack()
    
    tk.Frame(marco_central, height=30, bg="white").pack()
    
    campos = [
        {"label": "Correo electrónico", "show": "", "icon": "✉️"},
        {"label": "Contraseña", "show": "*", "icon": "🔒"}
    ]
    entries = []
    
    for campo in campos:
        frame = tk.Frame(marco_central, bg="white")
        frame.pack(fill="x", pady=8)
        
        tk.Label(
            frame,
            text=f"{campo['icon']} {campo['label']}",
            bg="white",
            fg=color_texto,
            font=("Segoe UI", 10),
            anchor="w"
        ).pack(fill="x")
        
        entry_frame = tk.Frame(frame, bg=color_borde, height=2)
        entry_frame.pack(fill="x", ipady=2)
        
        entry = tk.Entry(
            entry_frame,
            font=("Segoe UI", 12),
            bg="white",
            relief="flat",
            borderwidth=0,
            show=campo["show"],
            highlightthickness=0
        )
        entry.pack(fill="x", padx=5, pady=5)
        entries.append(entry)
        
        def on_enter(e, f=entry_frame):
            f.config(bg=color_principal)
        
        def on_leave(e, f=entry_frame):
            f.config(bg=color_borde)
        
        entry.bind("<FocusIn>", on_enter)
        entry.bind("<FocusOut>", on_leave)
    
    tk.Frame(marco_central, height=10, bg="white").pack()
    
    def funcion_boton():
        correo = entries[0].get()
        contrasenna = entries[1].get()
        
        if not correo or not contrasenna:
            messagebox.showerror("Error", "Todos los campos son requeridos")
            return
            
        consultar_usuario = conectar(f"SELECT * FROM usuario WHERE correo = '{correo}' AND contraseña = '{contrasenna}'")
        
        if len(consultar_usuario) != 0:
            ventana.destroy()
            ventana_usuario("hola soy el usuario")
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    btn_login = tk.Button(
        marco_central,
        text="INICIAR SESIÓN",
        command=funcion_boton,
        bg=color_principal,
        fg="white",
        font=("Segoe UI", 12, "bold"),
        relief="flat",
        bd=0,
        padx=30,
        pady=12,
        activebackground=color_secundario,
        cursor="hand2"
    )
    btn_login.pack(fill="x", pady=(10, 5))
    
    
    def on_enter_btn(e):
        btn_login['background'] = color_secundario
    
    def on_leave_btn(e):
        btn_login['background'] = color_principal
    
    btn_login.bind("<Enter>", on_enter_btn)
    btn_login.bind("<Leave>", on_leave_btn)
    
    
    tk.Label(
        marco_central,
        text="¿No tienes una cuenta? Contacta al administrador",
        font=("Segoe UI", 9),
        bg="white",
        fg="#64748b",
        pady=20
    ).pack()